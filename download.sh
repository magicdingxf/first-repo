#!/bin/bash
#检查网络连通性

materials_address=172.25.72.248:8033
materials_ak=vkjWeAst0l4xrza5tpzf
materials_sk=QZAG4LAgMhV8u0E58Wg7mV95MoVZSYtWe1s3T5T0
materials_alias=pkgsphere-800
cz_cpu_arch=amd64

cmd_path=./.pkgsphere_cmd
# 创建临时目录
if [ ! -d "$cmd_path" ]; then
	if mkdir -p $cmd_path; then
		echo "创建临时目录成功"
	else
		echo "创建临时目录失败"
		exit 1
	fi
fi
download_url=http://$materials_address/share/darwin/mc
yq_download_url=http://$materials_address/share/darwin/yq
mc_command=mc
yq_command=yq
# 判断操作系统类型
if [[ "$(uname)" == "Darwin" ]]; then
    echo "当前操作系统是 Mac OS X"
	if [[ "$(uname -m)" == "arm64" ]]; then
		download_url=http://$materials_address/share/darwin-arm64/mc
		yq_download_url=http://$materials_address/share/darwin-arm64/yq
	else
		download_url=http://$materials_address/share/darwin-amd64/mc
		yq_download_url=http://$materials_address/share/darwin-amd64/yq
	fi
elif [[ "$(uname)" == "Linux" ]]; then
    echo "当前操作系统是 Linux"
	if [[ "$(uname -m)" == "arm64" ]]; then
		download_url=http://$materials_address/share/linux-arm64/mc
		yq_download_url=http://$materials_address/share/linux-arm64/yq
	else
		download_url=http://$materials_address/share/linux-amd64/mc
		yq_download_url=http://$materials_address/share/linux-amd64/yq
	fi
elif [[ "$(uname)" == *NT* ]]; then
	echo "当前操作系统是 Windows"
	if [[ "$(uname -m)" == "arm64" ]]; then
		echo "当前操作系统 windows arm64 不支持"
    	exit 1
	else
		download_url=http://$materials_address/share/windows-amd64/mc.exe
		yq_download_url=http://$materials_address/share/windows-amd64/yq.exe
	fi
else
    echo "无法确定当前操作系统"
    exit 1
fi

# 下载mc
if type mc > /dev/null 2>&1; then
    echo "mc 命令已经存在，配置别名pkgSphere"
	mc alias set $materials_alias http://$materials_address $materials_ak $materials_sk
	if [ $? -ne 0 ]; then
		echo "配置别名pkgSphere 失败,请检查mc命令是否为minio客户端程序 ex: mc alias ls"
		exit 1
	fi
else
	if [[ "$(uname)" == *NT* ]]; then
		echo "mc 命令不存在开始下载"
		curl --progress-bar -o $cmd_path/mc.exe $download_url
		chmod +x $cmd_path/mc.exe
		$cmd_path/mc.exe alias set $materials_alias http://$materials_address $materials_ak $materials_sk
		mc_command=$cmd_path/mc.exe
	else
		echo "mc 命令不存在开始下载"
		curl --progress-bar -o $cmd_path/mc $download_url
		chmod +x $cmd_path/mc
		$cmd_path/mc alias set $materials_alias http://$materials_address $materials_ak $materials_sk
		mc_command=$cmd_path/mc
	fi

fi

# 下载yq
if type yq > /dev/null 2>&1; then
    echo "yq 命令已经存在"
else
	if [[ "$(uname)" == *NT* ]]; then
		echo "yq 命令不存在开始下载"
		curl --progress-bar -o $cmd_path/yq.exe $yq_download_url
		chmod +x $cmd_path/yq.exe
		yq_command=$cmd_path/yq.exe
	else
		echo "yq 命令不存在开始下载"
		curl --progress-bar -o $cmd_path/yq $yq_download_url
		chmod +x $cmd_path/yq
		yq_command=$cmd_path/yq
	fi

fi


# 函数：检查远端文件和本地文件大小并进行复制
function copy_if_different() {

	local cm_local=$1
    local remote_alias=$2
    local remote_file=$3
    local local_file=$4

    if [ -z "cm_local" ] || [ -z "$remote_alias" ] || [ -z "$remote_file" ] || [ -z "$local_file" ]; then
        echo "Usage: copy_if_different <cm_local> <remote_alias> <remote_file> <local_file>"
        return 1
    fi

    # 获取远端文件大小
    remote_size=$("$cm_local" stat --json "$remote_alias/$remote_file" | "$yq_command" '.size')

    if [ $? -ne 0 ]; then
        return 1
    fi

    if [ -f "$local_file" ]; then
        # 获取本地文件大小
        local_size=$("$cm_local" stat --json "$local_file" | "$yq_command" '.size')

        if [ "$remote_size" != "$local_size" ]; then
            # 大小不同，复制远端文件到本地
			return 1
        else
            # 大小相同，不需要复制
			return 0
        fi
    else
        return 1
    fi
}

# 全部物料
all_materials=("charms/docker-iam-bce-login-3.2.1.37-charm.tar.gz")
# 下载物料

function download() {
    # 下载物料
    for material in ${all_materials[@]}; do
    	if [[ $material == charms* ]]; then

			copy_if_different $mc_command  $materials_alias $material ./$material
            diff_result=$?
			if [[ "$diff_result" -eq 0 ]]; then
				echo "$material 已经存在跳过"
				continue
			fi
			
			# 下载charms
    		$mc_command cp  $materials_alias/$material ./$material
    		if [ $? -ne 0 ]; then
    			echo "$material 下载失败"
    			return 0
    		fi

    	fi

        if [[ $material == dockers* ]]; then
    		$mc_command mirror  $materials_alias/$material/docker ./docker
    		if [ $? -ne 0 ]; then
    			echo "$material 下载失败"
    			return 0
    		fi
        fi

    	if [[ $material == bcc* ]]; then

			copy_if_different $mc_command  $materials_alias $material ./$material
            diff_result=$?
			if [[ "$diff_result" -eq 0 ]]; then
				echo "$material 已经存在跳过"
				continue
			fi
    		$mc_command cp  $materials_alias/$material ./$material
    		if [ $? -ne 0 ]; then
    			echo "$material 下载失败"
    			return 0
    		fi
        fi

    	if [[ $material == cangzhu* ]]; then
    		$mc_command mirror --remove $materials_alias/$material ./cangzhu
    		if [ $? -ne 0 ]; then
    			echo "$material 下载失败"
    			return 0
    		fi
        fi

    	if [[ $material == resource* ]]; then

    		if [[ "$material" == */ ]]; then
				
				material=$(echo "$material" | awk '{sub(/\/+$/, ""); print}')
    			$mc_command mirror $materials_alias/$material ./$material
    			if [ $? -ne 0 ]; then
    				echo "$material 下载失败"
    				return 0
    			fi
    		else

				copy_if_different $mc_command  $materials_alias $material ./$material
            	diff_result=$?
				if [[ "$diff_result" -eq 0 ]]; then
					echo "$material 已经存在跳过"
					continue
				fi
    			$mc_command cp  $materials_alias/$material ./$material
    			if [ $? -ne 0 ]; then
    				echo "$material 下载失败"
    				return 0
    			fi
    		fi

        fi
    done

    return 1
}

download
download_success=$?

$mc_command alias remove $materials_alias
# 删除临时目录
rm -rf $cmd_path
if [ $? -ne 0 ]; then
	echo "$cmd_path 临时目录失败，请手动删除"
fi

if [ "$download_success" -eq 1 ]; then
  echo "下载完成 请按Ctrl + c 退出"
else
  echo "下载失败 请按Ctrl + c 退出 在日志文件中定位原因"
fi

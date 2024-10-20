##全局变量
title = '模块2'

##函数
def say_hello():
    print(f'我是 {title}')

class Cat():
    pass


##再日常开发中 需要测试当前模块所编写的代码
##当模块被导入时，根据当前的业务，自主选择你要运行的代码块
import ceshi


t1 = input('请输入是够有票，yes/NO \n')
if t1 == 'yes':
    tmp = float(input('请输入你的体温\n'))
    if tmp <=37.6:
        print('有票体温正常允许入站')
    else:
        print('有票体温不正常不允许入站')
else:
        print('无票不允许入站')
#print(tmp)

from  mokuai3 import qwtest
qwtest()
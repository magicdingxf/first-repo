def qwtest():
    print('some one user test')
if __name__ == '__main__':   ###被当作模块的时候，下面的代码不会被显示出来
    print('this  is a test')
"""
包
概念：包就是项目结构中文件夹/目录
作用：
包就是将有联系的模块放在同一个文件夹下，并且在这个文件夹下创建__init__.py文件，那么这个文件夹就称之为包，有效避免模块名称冲突问题
让结构更清晰。



"""
qwtest()

#from baotest import *
# import  baotest.register
# import baotest.another
from baotest import *
register.reg()
another.tha()
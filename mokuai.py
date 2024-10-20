"""
含义:
在python中一个py文件就是一个模块，里面定义了一些函数和变量，需要的时候可以导入并使用这些模块
执行步骤
1、在python模块记载路径中查找相应的模块文件
2、将模块文件编译成中间代码
3、执行模块文件中的代码

3.4
内置全局变量__name__
语法
if __name_ == '__main__': ##用来控制py文件在不同的应用场景执行不同逻辑

## 3.4.3
1\文件在当前程序执行（自己执行自己）__name ==__mian__
2\文件被当作模块被其他文件导入 __name == 模块名



random  time .os  logging 直接导入即可使用
1、内置模块

2、第三方模块
 下载 cmd窗口 输入 pip install  模块名
3、自定义模块
自己在项目中定义的模块,注意命名要遵循命名规范，不要与内置模块重名
导入方式
##注意不建议多食用from。。。IMPort 声明  有时候命名冲突会造成一些长偶五
from pytest import *

as 给模块起别名

"""
import thetest1
#thetest1.say_hello()

from thetest2 import say_hello   ##导入函数只需要函数名
from thetest1 import say_hello as  shi

#shi()
#say_hello()

#import pytest as pt1
#from pytest import  funa as a,name,funb as b  ##导入多个功能，使用逗号 将功能与功能隔开
##pt1.fail()
#from pytest import *

#from pygame import *


import baotest



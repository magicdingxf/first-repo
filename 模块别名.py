import thetest1 as mt1
import thetest2 as mt2


###别名只是在当前文件中使用，临时的名称，方便模块的调用
mt1.say_hello()
print(mt1.__file__)
mt2.say_hello()


##from ....import 导入
"""
如果希望从一个模块中，导入部分工具，就可以使用from ...import的方式
import 模块名，是一次性把模块中所有工具全部导入，并且通过 模块名/别名 访问

导入后不需要通过模块名，可以直接使用模块提供的工具，全局变量，函数，类

如果两个模块，存在同名的函数，那么后导入的模块的函数，会覆盖掉先导入的函数



"""
##模块 from..import



## from test1 import *  ##导入所有
from thetest1 import say_hello as sayhi1
sayhi1()

from thetest1 import Dog
from thetest2 import say_hello as sayhi2
sayhi2()
d1 = Dog()
print(d1)



###创建一个类对象
####我们在创建python文件中，不要将文件名与python解释器中的内置的方法重名
import random
print(random.__file__)

###输出路径 /Users/dingxiangfa/anaconda3/envs/pythonProject/lib/python3.11/random.py

### 搜索当前目录指定模块的文件，如果有就直接导入，如果没有，再搜索系统目录


rand =random.randint(0,10)
print(rand)

rand2 = random.randint(100,200)
print(rand2)

"""
原则---每一个文件都应该可以被导入
一个独立的python 文件就是一个模块

"""




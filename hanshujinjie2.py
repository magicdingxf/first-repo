"""
作用域：变量生效的范围，分别为全局变量和局部变量
1.2全局变量
函数外部定义变量，在整个文件中都是有效的

局部变量
函数内部定义的变量，从定义的位置开始到函数结束的位置有效

全局变量和局部变量命名相同，局部变量不会被覆盖
"""

a = 100
def test():
    print('这是test1中a的值',a)
test()

def test2():
    a = 120
    print('这是test1中a的值', a)##如果要使用变量，优先在函数内部找，局部变量
test2()   ###

def func():
    global num1,age
    num1 = 20
    print('这是test1中a的值', num1)
func()  ###
print(num1)  ###必须调用完完函数global函数才能声明，如果不调用无法使用全局参数
func()
##print(num)  ###局部变量只能在函数内部使用，
###在含糊内部修改全局变量的值，可以使用glogal 关键字
##将变量声明为全局变量
##global关键字可以对全局变量进行修改，也可以在局部作用域声明全局变量
"""
nonlocal ---了解，用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数进行声明，内部函数用nonlocal声明


"""

a = 10
def outer():
    a = 5
    def inner():
        print('intera的值',a)
    inner()
    print('outera的值', a)
outer()    ##输出内部的a = 5

def outer():
    def inner():
        a = 5
        print('intera的值',a)
    inner()
    print('outera的值', a)  ##输出外部的变量10
outer()  ##输出外部的

def outer():
    a = 12
    def inner():
        nonlocal a  #只对上一级进行修改，只改变外层函数的值
        a = 20
        print('intera的值',a)
    inner()
    print('outera的值', a)  ##输出外部的变量10
outer() #输出20

"""
匿名函数 lambda
lamdbda 形参：返回值
调用：结果 = 函数名（实参）
lamdbda 不需要写return 来返回值，表示本身结果就是返回值
"""
def add(a,b):
    return (a+b)
s = lambda a,b:a+b  ##a,b 是匿名函数的形参,a+b 是返回值的表达式

print(s(12,23))

"""
lamdbda 参数格式

"""

funa = lambda :'一桶水果茶'
print(funa())
funb = lambda name:name
print(funb('mading'))
func = lambda name,age=18:(name,age)
print(func('sdsds'))
print(func('sdsds',20))
fund = lambda a,b,c:(a+b+c)
print(fund(12,2,3))
"""可变参数"""
fune = lambda **kwargs:kwargs
print(fune(name='dada',age=20))

"""
lambda结合if判断
三目运算
lambda只能实现简单的逻辑，如果逻辑复杂且代码量较大， 不建议使用lamdba 降低代码的可读性


"""
a = 5
b = 12
print('a<b') if a<b else print("a>b")

comp = lambda a,b:"a<b" if a<b else 'a>b'
print(comp(32,12))
"""
内置函数
 查看所有的内置函数
 import builtins
dir()函数不带参数时，返回当前范围内的变量，方法和定义的类型列表：
带参数时，返回参数的属性，方法列表，如果参数包含方法 __dir()__ 该方法将被调用

"""
print(dir())
##输出结果  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'add', 'b', 'comp', 'funa', 'funb', 'func', 'fund', 'fune', 'num1', 'outer', 's', 'test', 'test2']
##获取当前模块的属性列表

print(dir([1,2,3])) ###查看列表的方法



import builtins
print(dir(builtins))
###大写字母开头一般是内置常量名，小写字母开头一般是内置函数名
"""
内置函数
abs()返回绝对值
sum() 求和
min()最小值
max()最大值
zip()将可迭代对象作为参数，将对象中的元素打包成元祖
map 空间   可以对可迭代对象的每一个元素进行映射，分别去执行
reduce()对参数序列中的元素进行累积            

"""

print(sum([1,2,12]))    ##sum函数要放可迭代对象，求和只能int类型
print(sum({1,2,12}))    ##sum函数要放可迭代对象，求和只能int类型
print(sum((1.5,2,12)))   ##只要有1个浮点数，结果必然是浮点数

print(min([1,2,12]))
print(min({12,22,12}))
print(min(-8,5,key=abs))   ###绝对值比较，先求绝对值，再比较

print(type((1.5,2,12)))  ##元祖 。

li = [1,2,3]
li2 = ['a','b','c']
l3 = {a:2,b:5}
l4 = [13,24,35]
print(zip(li,li2))
def func(x):
    return x*5

####如果元素个数不一致，按最短的返回确认
for i in zip(li,li2):
    print(i)
print(type(i))

mp1 = map(func,li)  ##只需要写函数名不需要小括号
mp2 = map(lambda x:x*6,li)   ##使用匿名函数表示
print(mp1)
for i in map(func,li):  ###用for循环取出
    print(i)

print(list(mp1))  ###转换成列表输出
print(list(mp2))
mp3 = lambda x,y:x+y
print(mp3(12,23))
m3 = map(mp3,li,l4)
print(list(m3))
print(list([2,3,4]))
print("**************")
print(list(m3))  ##打印为[]
m4 = map(lambda x,y:x*y,[1,2,3],[2,3,4])
"""
m4 是一个迭代器，一旦被迭代（如上例中的 print(list(m4))），它就被消耗了。  
# 再次尝试迭代 m4 将不会得到任何结果，因为它已经空了
"""
print(list(m4))   ##打印[2,6,12]
print(list(m4))  ###打印[] m4被消耗了，所以无值

"""
reduce()先把对象中的两个元素取出，计算出一个值然后保存着，接着把计算值跟第三个元素计算

"""
print("*********reduce***************")
from  functools import reduce  ##import reduce


def add(a,b):
    return a+2*b
c= [1,2,3,4,5,6]
d = reduce(add,c)   ##function 函数必须是有2个参数的函数，squence 序列 可迭代对象
print(d)   ##输出21 ，c的列表值相加

d2 = reduce(lambda x,y:x*y,c)
print(d2)   #输出720 ==6！
##拆包
##含义:对于函数中多个返回数据，去掉元祖，列表或者字典，直接获取里面数据的过程

tua = (1,2,3,4,5)
##方法1 ，
a,b,c,d,f = tua  ###元祖内有多少数据，前面就要有几个变量 接收
##这种方法一般在获取元祖值的时候使用
print(a,b,c,d,f)
##方法二
a,*b = tua
print(a,b)   ##输出 1 [2, 3, 4, 5]
s,d,f,r = b
print(s,d,f,r)  ##输出 2, 3, 4, 5


##一般在函数调用时
def funs(a,b,*args):
    print(a,b)
    print(args,type(args))
funs(1,2,3,4,5,12,343)  ##先把单独的取出来，其他都交给*的变量
arg = (6,7,8,9,10,11,12,13)
funs(*arg)






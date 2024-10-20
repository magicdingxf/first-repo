"""
定义“
将具有独立功能的代码块组织成一个整体，使其具有特殊功能的代码集
作用：
使用函数可以加强代码的复用性，提高程序编写的效率
结构：
def 函数名（）:
    函数体

函数名要符合标识符规定，最好见名知义
返回值 return
函数执行结束后，最后给调用者的一个结果
作用
return会给函数的执行者返回值


"""

def buy1():
    return "buy some thing",23  ##,可以返回多个值，函数中遇到return ,return之后的不会被执行
    print('hello')

print(buy1())  ##return返回多个值，以元祖的形式返回给调用者
buy1()

##返回值的三种情况总结
"""
一个返回值也没有，返回结果是none
2、一个返回值就把值返回给调用者
3、多个返回值，以元祖的形式返回给调用者

##return和print
return表示函数结束，print会一直向下执行
return是返回计算值，print是打印结果
"""

def fumm():
    return 123
    print(123)
print(fumm())

def add():
    a=1
    b=2
    print(a+b)
    return (a+b)
print(add())
"""
参数
def 函数名(形参a,形参b):
    函数体
    
    



"""

def add(a,b):
    return a+b
print(add(12,34))
print(add('s','y'))
print(add([1,2,3],[4,5,6]))
print(add((1,2),(4,5)))
print(type((1,2)))
#print(add({1,2,3},{2,3,4}))
s1 = {2,3,4}
a1 = {2,3,1,5,6,7}
print(id(s1))
s1.update(a1)
print(id(s1))  ##内存地址没发生变化
"""
不可变数据类型
整数，浮点，字符串、元祖、布尔

可变数据类型
字典、列表、集合
"""

print(s1)
s1.add(15)
print(s1)
s2 = (4,5,6,7,8)
s3 = s2+(6,8,9,12)
print(s3)


"""
默认参数
含义，为参数提供默认值，调用函数时可不穿该默认参数的值
注意：所有的位置参数必须出现在默认参数钱，包括函数定义和调用
格式：
def func(a=12):



可变参数
传入的参数值的数量是可以改变，可以传入多个，也可以不传

"""

def func(a=12):  ##参数为a，如果没有传值，用默认参数
    print(a)
func()
func(200)

def func(c,b,a=5,d='f'):
    pass


def funs(*args):  ###可变参数，*具有特殊含义，以元祖的形式接受,可以把args改成其他参数，但是args更符合代码规范性
    print(args)

funs(1,2)
funs('name','wuli')
funs()


###关键字参数，**args
def funx(**kwargs): ##关键字参数，以字典的形式接受，
    print(kwargs)
funx(age=12,name='qwq')   ##传值的时候，需要采用key=value的形式传入
##可以扩展函数的功能


"""
函数嵌套
函数调用，在一个函数里面调用另外一个函数


"""

def study():
    print('晚上在学习')
def course():
    study()
    print('学习python基础')
course()

def student():
    print('某个学生')
    def learn():
        print('在学习课程')
    learn()  ##注意缩进，定义和调用是同级的，不要在内层函数调用外层函数，会陷入死循环
student()   ###如果没有内函数的调用，只会打印外函数

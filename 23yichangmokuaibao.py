"""
23异常，模块 包
异常
定义：程序执行过程中出现的非正常流程现象


1.NameErro:使用一个还未被赋值的变量
2.SyntaxError:代码不符合python语法规定
3.IndexError:下标/索引超出范围
4.ZeroDivisionError:0
5.KeyError:字典里不存在这个键
6.IOError:输入/输出操作失败，基本上是无法打开文件（比如你要
读的文件不存在)
7.AttributeError:对象没有这个属性
8.ValueError:传的值有错误
9.TypeError:类型错误，传入的类型不匹配
10.ImportError:无法引入模块或包；基本上是路径问题或名称错
误
11.IndentationError:缩进错误；代码没有正确对齐

异常的处理：
方式一：根据控制台的错误提示找到出错点并分析改正
方式二，对异常进行捕获处理
try：
    不确定是否能够正常执行的代码
except:
    如果检查到异常就执行这个位置的代码

"""

## abc =     ##SyntaxError
# abc =12
# try:
#     print(eval('print(abc*)'))
# except (SyntaxError):
#     print('语法错误')

# globals_dict = {}
# locals_dict = {}
#
# exec("""
# x = 5
# def add(a,b):
#     return a+b
# """,globals_dict,locals_dict)
#
# #print(globals_dict['x'])
# print(locals_dict['add'],(2,3))
#globals（可选）：一个字典，用于指定全局命名空间的符号表。如果未提供该参数，则使用当前全局符号表。

#locals（可选）：一个字典，用于指定局部命名空间的符号表。如果未提供该参数，则使用与 globals 参数相同的值。

#下面是 exec() 函数的使用示例：

globals_dict = {}
locals_dict = {}

exec("""  
x = 5  
def add(a, b):  
    return a + b  
""", globals_dict, locals_dict)

# print(globals_dict['x'])  # 输出: 5
# print(locals_dict['add'](2, 3))  # 输出: 5

d1 = {'name':'mali','age':18}
print(d1)
print(d1['name'])


# abc =     ##SyntaxError
abc =12
try:
    print(int(abc+'dda'))
except (SyntaxError,TypeError): ##当要捕获多个异常类型时，可以把要捕获的异常类型的名字放到except后，并以元祖的形式保存
    print('语法错误')

"""
try:
    可能会引发异常的代码
except:
    出现异常现象的处理代码
else:
    没有捕获到异常执行的代码
    
    
Exception是Python中所有异常的基类，几乎所有的异常都是它的子类（或子类的子类）。
因此，使用except Exception:可以捕获到几乎所有的异常，但通常不建议这样做，
因为它会捕获包括KeyboardInterrupt（用户中断，如Ctrl+C）在内的所有异常，这可能会隐藏你不想忽略的错误。
"""
print('***********except else **************')
try:
    print('abc')
except Exception:
    print('这一行代码有错误')
else:
    print('这里是else代码')  ###try和else是一起执行，没有报错的情况下就会向下执行else语句

print('***********exception as **************')
try:
    print(abcd)
except Exception as e:
    print(f'这一行代码有错误 {e}')
else:
    print('这里是else代码')
print('************finally********************')
l1 = [1,2,3,4]
try:
    print(l1[3])
except Exception as e:
    print(f'语法错误 {e}')   ###程序异常才会执行
else:
    print("try的语法没有问题")  ##程序正常才会执行
finally:
    print('程序执行结束')      ###无论程序是否异常都会执行该语句
##可以单独使用try finally
try:
    print(l1[4])
except Exception as e:
    print(f'语法错误 {e}')

finally:
    print('程序执行结束2')

"""
抛出异常 raise 
步骤：
创建一个exception('xxx‘)对象，xxx异常提示信息
2、raise抛出这个对象，异常对象

"""

def funx():
    print('hahahah')
    raise Exception('冰冰抛出一个异常')  ##执行了raise语法后面的语句不会继续执行
    print('no good')
#funx()
def login():
    pw = input('请输入一个密码\n')
    if len(pw) > 8:
        return '密码输入正确'
    else:
        raise Exception('输入的密码长度不够8位')
#login()####不会打印只会返回
#print(login())   ###可以打印返回值
try:
    pw = input('请输入一个密码\n')
    if len(pw) > 8:
        print('密码输入正确')  ##不能使用return ，在脚本（非函数）的顶层使用 return 会导致 SyntaxError，因为脚本的顶层不期望有返回值。
    else:
        raise Exception('输入的密码长度不够8位')
except Exception as e:
    print(f'错误信息：{e}')

##捕获异常是位检测到异常时，代码还能继续往下运行，程序不会终止



print('wwwwwwwwwwwwwwwwwwwwwwwwwww')
# try:
#     print(l1[4])
# except Exception as e:
#     print(f'语法错误 {e}')
#     raise Exception('语法错误')
#
# finally:
#     print('程序执行结束2')
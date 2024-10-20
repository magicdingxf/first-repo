def say_hello():
    print('你好')
##测试入口
if __name__=='__main__':
    print('小明开发的模块接口')
    say_hello()

##如果再当前文件中执行的话， __name__属性会变成 __main__ 字符串
""""
如果在其他的文件执行时，__name__ 就不等于__main__
"""


##全局变量
title = '模块1'

##函数
def say_hello():
    print(f'我是 {title}')

class Dog():
    pass

print('this is a test','shugndong','shenme',sep='|')
print('this sas','dsds',end='后面拼接的是')
print('sdhunt',end='----')
print('sdsdssd')
####复数complex= 实部+虚部 ,虚部单位只能是j,不能是其他的 否则报错,可以不区分大小写
a1=2+3j
print(type(2+4j))   ##<class 'complex'>
a2=4+5J
print(a1+a2)

###   %s %d %f
print('my name is %s.' % 'lihua')
print('my age is %d' % 18)
age1 = 24
##%f 默认6位消暑，遵循四舍五入原则
## %7f 显示7位消暑
print('%f'% 0.1212)
##数字设置位数，不足前面补空白， %04d ,不足补0
print('my age is %04d'%age1)

print('this is %%的 1%%' % ())  ##this is %的 1%

print(f'this is {age1}')

print(range(5))
for i in range(5):
 #   print(i)
    pass
print(i)
print(r'thi is a \\\\test')###r表示不转义

# age2 = int(input('请输入你的年龄\n'))
# if age2 > 18:
#     print('可以上网')
# else:
#     print('不可以上网')


###and  or  not   与或非
a1 = 'nihao'
a2 = 'wohao1'
if a1=='nihao' or a2=='wohao':
    print('ni and wo hao')

print( not 3>9)
##三目运算

if a1 == 'nihao':
    print('right')
else:
    print('wrong')


##三目运算
print('right') if a1==a2 else print('wrong')

print('good') if (10>1) else print('bad')

score = int(input('请输入你的分数\n'))
if    80 <=score<= 100:
    print('great work')
elif  60 <=score<80:
    print('good performance')
else:
    print('you need work hard')

import test_

test_.send_message.sendm('你好')

print(test_.receive_message.receive())

""" 我们需要在__init__.py文件下声明提供的模块"""
for i in range(0,100):
    print(i,'您好')

# i = 1
# while i <100:
#     print(i,'我不好')
#     i+=1
# #break 和continue 只能放在循环里

i=1
while i <5:
    print(f'eating {i} apple')
    if i==3:
        print('i am full')
        break   ##条件满足时退出循环
    i+=1

##continue 退出本次循环进行下次循环

i=1
while i <6:
    print(f'eating {i} apple')
    i += 1
    if i ==3:
        print(f'{i}苹果吃到虫子')
        i+=1
        continue   ##跳过3，结束在3的循环，在continue之前一定要修改计数器，否则会陷入死循环=



a = 'helllo'
print(a)
a1 = a.encode()
print(a1)
print(type(a1))   ###class bytes

a2 = a1.decode()
print(a2)
s1 = '这里是python学习'
a3 = s1.encode("utf-8")
print(a3,type(a3))

if 'su' in 'sudansuda':
    print('you are ring')


a= 10
b = 5
print('a=',id(a))
print('b=',id(b))
a,b = b,a

print('交换后a=',id(a))
print('交换后b=',id(b))
print(a)
print(b)

st1 = 'i love CHINA LONG TIME LAST lonely lenth'
print(st1[1:4])
print(st1[-1:-5:-1])
print(st1[::-1])

##修改元素，replace()替换s
st2 =st1.replace('l','m',1) ##t替换1次，不加就全部替换
print(st2)

##split 指定分隔符替换
st3 = st1.split(' ')
st4 = st1.split(' ',1) ##只分隔一次
print(st3)   ##以列表的形式输出分隔后的结果，['i', 'love', 'china', 'long', 'time', 'last', 'lonely']
print(st4)

##capitalize 首字母字符大写，其他都小写
##upper 全部大写
##lower 全部小写
print(st1.capitalize())
print(st1.upper())
print(st1.lower())
print(st1.find('i'))   ##返回中查找的索引值
print(st1.find('L',2,8))  ##包前不包后，找不到返回-1
q2 = 'abcdefabcdef'
print(q2.find('e',1,4))
print(q2.find('m',1,4))###找不到返回-1
print(q2.index('ab'))
print(q2.index('fab'))
print(q2.index('e',1,18))
print(q2.count('f'))
print('*****')
print(q2.find('e',1,10))
import re
q3 = 'abcdefabcdef'
q4 = 'de'
matches = re.finditer(q4,q3)
p1 = [match.start() for match in matches]
print(p1)

print(q3.startswith('ab',1,12))
print(q3.endswith('def',1,19))
match = re.search(q4,q3)
# print('********')
# print(match)
# p2 = [match.start() for match!=null]
# print(p2)


names = ['lilei','sundong','samb','huahua','aaa']
# while True:
#     name =str(input('请输入你的账号\n'))
#     if name in names:
#         print('您输入的账号已被占用')
#     else:
#         print(f'您的用户名为 {name} ')
#         names.append(name)
#         break
# print(names)

print(names.index('lilei'))  ###返回指定数据所在位置的下标，如果查找的数据不存在，则会报错
print(names.count('a'))  ##count,统计数据在当前列表中出现的次数

print(q3.count('ab'))
names.insert(3,'mali')  ###在指定位置插入元素
names.append('sunming')###append集体添加
names.extend('wuhan')###分散添加，将'wuhan'中的元素逐一添加
names.extend(['deti','furi'])  ###将['deti','furi'] 的元素添加到列表中
names.extend(('detis','furie'))  ###将['deti','furi'] 的元素添加到列表中
print(names)

##列表的删除 del. pop,remove
l1 =['a','d','d','fd','asa','ewewe']
##del l1   ###删除列表之后无法print
del l1[1]
print(l1)
l1.pop()  ###默认删除最后一个
print(l1)
l1.pop(2)  ###下标值不能超过列表元素小标范围
print(l1)
l1.remove('d')  ###默认删除最开始出现的元素
print(l1)

##排序  sort 默认从小打到，
w1 = [1,2,34,121,223,12,32,54,444]
w1.sort()  ###sort 从小到达的顺序排序
print(w1)  ###
w2 = [1,2,34,121,223,12,32,54,444]
w2.reverse()  ##将整个列表倒过来
####
print(w2)
w2.sort()
w2.reverse()    ###2个方法一起用就是倒序排列
print(w2)

###列表推倒式

##格式一，[表达式 for 变量 in 列表]
##注意 ，in后面不仅可以放列表，还可以放range()可迭代对象
li2 = [2,3,4,5,6,7]
print([i*2 for i in li2])
print(li2*2)
[w2.append(i) for i in li2]
print(w2)

##格式二 [表达式 for 变量in 列表 if条件]
l3=[]
for i in li2:
    if i%2!=0:
        l3.append(i)
print(l3)

[l3.append(i) for i in li2 if i%2==0]
print(l3)


###列表嵌套

l3 = [1,2,3,4,5,6,[7,8,9]]
print (l3[6][1])

"""
元祖
基本格式：元祖名=（元素1，元素2，...）
所有的元素都在小括号内，元素与元素之间用，隔开，不通元素也可以是不通数据类型
元祖只支持查询操作，不支持增删改
"""

tp1 = ()  ##定义空元组
print(type(tp1))

tp2 = (21,2,3,4)
print(tp2[2])
##count(),index(),len()
print(len(tp2))
print(tp2[1:3])  ##切片
"""
函数的参数和返回值
格式化输出的（）本质上是一个元组
数据不可以修改的时候
"""
name = 'sunbing'
age = 19
print("%s 的年龄是 %d"% (name,age))
info = (name,age)
print('%s 的年龄是%d' % info)

##字典  d1 = {k1:v1,k2:k2} ,key必须是唯一性，否则会被最后的key替换

dc1 = {'name':'mali','age':19}
print(dc1['name'])
###d1.get(key)
print(dc1.get('age'))  ##或者value值
print(dc1.get('des','no-value'))  ###取某个key，如果不存在，返回默认值
##修改元素
dc1['name']='wudan'  ##修改，键名存在就修改，不存在就新增
print(dc1['name'])
dc1['grade']='hight2'
print(dc1)
dc2 = {'dan':'ent','sha':'chama'}
dc1.update(dc2)
print(dc1)

del dc2   ##删除后，字典不存在，无法被打印# 就会报错
#print(dc2)
del dc1['age']
print(dc1)

##clear()清除整个字典里的东西，但是保留该字典
dc1['name']='fufu'
print(dc1)
dc1.pop('name')

print(dc1)
dc1.popitem()
print(len(dc1))
print(dc1.keys())
for i in dc1.keys():
    print(i)

print(dc1.values())

for i in dc1.values():
    print(i)

for i in dc1.items():   ##打印字典
    print(i)

##集合是无序的，元素唯一性 自动去重，利用无序性，不能修改，
#基本格式 集合名={元素1，元素2，元素3。。。}
a1 = {19,20,33}
s2 = {}##空字典
s3 = set()
print(type(s2))
print(type(s3))  ##集合

##python中int整型的hash值就是它本身，在hash中不会变化

s4 = {1,2,3,4,32,4}
print(s4)
##集合添加元素
s4.add('madan')
s4.add((35,34))   ##当作一个元素传进去
print(s4)
s4.update(a1)   ##添加可迭代对象，将传入的元素拆分，一个个放到集合中
print(s4)
s4.pop()   ##pop默认根据hash表排序后的第一个元素，对集合仅需无序排列，然后将左边的第一个元素删除
print(s4)
s5 = {'a','b','c','d','des'}
s5.pop()          ####pop无序删除
print(s5)
s4.pop()
print(s4)
s4.remove(3)
print(s4)
s4.remove('madan')
print(s4)

##discard 选择要删除的元素，有就会删除，没有则不会进行任何操作
s4.discard('33')
print(s4)
s4.discard(33)
print(s4)

###交集和并集
a2 = {1,2,3,4}
b2 = {2,3,4,5,6,7}
c2 = {343,12123,4343}
print(a2&b2)       ##返回共有部分
print(a2&c2)

##并集，将所有元素都放一起
print(a2|c2)
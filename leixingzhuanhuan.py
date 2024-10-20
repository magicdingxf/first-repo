import copy

a1 = 1.2323
print(int(a1))   ##如果字符串中有数字和正负号以外的字符就会报错
print(int('-1992'))
###float 转换成str会取出末位为0的小数部分


print(str(-1.00))
##将列表转换成字符串
l1 = [1,2,3]
l2 = str(l1)
print(type(l2))
##执行运算并返回运算的值
print(eval('10+10'))
print(eval('10'+'10'))  ##整数和字符串不可以相加
##eval 可以实现list, dict  ,tuple和str的相互转换
st1 = "[[1,2],[3,4],[5,6]]"
print(type(st1))
l1 = eval(st1)   ##将字符串转换成列表，
print(l1)
print(type(l1))

str1 = "{'name':'mali','age':18 }"
dct1 = eval(str1)  ##将字符串转换成字典
print(dct1)
print(type(dct1))

#eval 非常强大，但不够安全

##list将可迭代对象转换成列表
##支持转换成list的类型，str,typle dict set

print(list('adddaewewew'))  ##字符串转换成列表

print(list((1,2,3,4)))  ###数组转换成列表

##字典转换成列表，会取键名
##集合转换成列表，
print(list({1,2,3,4,'a','d',4}))
print('*************************')
##集合转换成列表会先去重
##深浅拷贝
li = [1,2,3,4]
li2 = li  ##将li直接赋值给li2
print(id(li))
print(id(li2))
li.append('sues')
print(li)
print(li2)
print('************************')
##赋值，会虽则会原对象一起变化 等于完全共享资源，内存地址一样

##浅拷贝 ，会创建新的对象，拷贝第一层是数据，嵌套层会指向原来的内存地址

li = [1,2,3,[4,5]]
li2 = copy.copy(li)
print(li2)
print(id(li))   ###内存地址不一样
print(id(li2))  ###内存地址不一样
li.append('9')
print(li)  ##只有li添加新元素
print(li2)

##外层的内存地址不通，但是内层的内存地址相同
li[3].append(7) ###嵌套列表添加新元素， li和Li2都新增
print(li)
print(li2)
print('*******************************')

###优点，拷贝速度快，占用空间少，拷贝效率高
###深拷贝，（数据完全不共享）外层的对象和内部的元素都拷贝了一遍

import copy

li = [1,2,3,4,12,343,[23,54]]
l2 = copy.deepcopy(li)  ##深拷贝,内外的内存都不一样，li变化，l2都不变
li.append('dongd')
print(li)
print(l2)
print(id(li[6]))
print(id(l2[6]))
print(li[-1])
li[-2].append('dsa')
print(li)
print(l2)
print(id(li))
print(id(l2))


###copy.deepcopy  ,不管是外层的还是内部的列表，内存地址完全不同，
print('*******************************')

##可变对象 变量对应的值可以修改，但内存地址不会发生变化 列表[]，字典{key:value}，集合{1,2,3} /
# 数组（）为非可变对象,

li = (1,2,3,4)   ##数组 不可变对象，无法操作
print(type(li))
print(id(li))

li = li+(32,45,12)
print(li)
print(id(li)) ##内存变化
print('*******************************')
li = {1,2,3,4}   #集合
print(type(li))
print(id(li))
li.pop()
print(li)
print(id(li))  ##集合内存地址没变

print('*******************************')
li = [1,2,3,[4,5]]
print(type(li))


print(id(li))
li.append('seu')
print(id(li))   ##内存地址不变
print('*******************************')
###不可变对象  含义，变量对应的值不能被修改，如果修改就会生成一个新的值，重新分配内存
n1 = 12
print(id(n1))
n1 = 18
print(id(n1))    ##内存地址发生变化

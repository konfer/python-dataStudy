# coding:utf-8

import copy
import numpy as np
import math
import matplotlib.pyplot as plt

t = (1, 2, 3)
print(type(t))

l = [1, 2, 3, 4]
type(l)
l.append(5)
print(l)

l.pop(3)
print(l)
l.append(6)
print(l)
print("del")
del l[1]
print(l)
print(len(l))

print(l[2])
print(l[2:4])
print(l[1:4])
print(l[0:4])
print(l[0:4:2])

# 是否为空
if not l:
	print("empty")
else:
	print("not emptyb")

s = "pythondjango"
print(s[1:5])

print("-----dict----")
myDict = {"jim": 18, "green": 19, "konfer": 20}
myDictOne = dict(a = 1, b = 2)
print(myDictOne.get('c', 'Default'))
myDict['d'] = 5  # 添加
print(myDict)
print(myDictOne)
print("---in dict test")
print("green" in myDict)

print(myDict.keys())
print(myDict.values())
print(myDict.items())
del (myDict["jim"])
print(myDict)

print("-----dict遍历----")
for key in myDict:
	print(myDict[key])

for key, value in myDict.items():
	print(key, value)

myDict.clear()
print(myDict)

html = '''
    <html>
    	<body>
    	<body>
    </html>ab
'''

print(html)

l = [1, 2, 3, 4]
print(l[len(l) - 1])
print(l[-1])
print(l[-len(l)])

a = [1, 2, 3]
b = [4, 5, 6]
d = [7, 8, 9]
print(id(a))
print(id(b))
c = a + b
print(c)
print(id(c))

print("--------")
print("---")
c.extend(d)
print(c)
print(c * 4)

e = [1, 2, 3]
e.append(4)
del e[2]
print(e)
g = [1, 2, 3, 4, 5]
print(g[1:4])
print("---index---")
print(g.index(2))

print(g[1:])
print(g[1:None])
print(g[:4])
print(g[::2])
h = "strip"
print(h[::-1])
print(h[::-2])

for i in a:
	print(i)

for index, value in enumerate(a):
	print(index, ":", value)

t = tuple(a)
print(t)
print(id(t))
print(id(a))

# ra = reversed (a)
# type(ra)
# for i in ra:
#	print rau
# print ra

s1 = ["hello", " everyone", ", we", "like", "python"]
print(" ".join(s1))

# tuple可修改
t3 = (1, 2, 3, [4, 5, 6])
t3[3].append(7)
print(t3)

# 浅拷贝---拷贝地址
p = [1, 2, 3, [4, 5, 6]]
q = p[:]
print(q)
p[3].append(7)
print(q)
print("p: ", p)
print(id(q[3]))
print(id(p[3]))

# 深拷贝---拷贝值
o = copy.deepcopy(p)
o[3].append(7)
print(o)
print("p:", p)

z = [y for y in range(10) if y < 5]
z2 = (y for y in range(10) if y < 5)  # 生成器
z1 = [(x, y) for x in range(3) for y in range(5)]
print(type(z1))
print(z1)
print("z2:", z2)


def f(x):
	return x % 5 == 0


fList = filter(f, range(1, 101))
print(fList)


def m(x):
	return x + 1


addedList = map(m, range(len(list(fList))))
print(addedList)

# for i in xrange(1, 10000):
#	print i

print(set([1, 2, 3, 2]))
print(set("element"))
mySet = set([1, 2, 3])

mySet.add(4)
print(mySet)
mySet.remove(2)
print(mySet)
mySet.update([5, 6, 7])
mySetSecond = set([1, 2, 3, 4])
print(mySet)
# print a|b
# print a-b
# bprint a^b

# 切片 （start:end:steps）
li = list(range(10))
print(li[2:8])
print(li[:4])
# 切片生成新类型bb

# 列表推导b
li = []
#	li.append(i)
print(li)

li = [1] * 10
print(li)

li = [i * 2 for i in range(10)]
print(li)

li_2d = [(0) * 3] * 3  # 引用3次
print(li_2d)

print("---------b")
s = (x for x in range(10))
print(s)

square_table = []
for i in range(50000):
	square_table.append(i * 1)

print("-------matrix---------")

myMatrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(myMatrix)
print(myMatrix.shape)
myMatrix.shape = 4, 3
print(myMatrix)
myMatrix.shape = 6, 2
print(myMatrix)

mySecMatrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype = np.float)
complexMatrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype = complex)
print(mySecMatrix)
print("------complexMatrix---")
print(complexMatrix)

MyThirdMatrix = myMatrix.reshape((4, -1))
print("first=\n", myMatrix)
print("second=\n", MyThirdMatrix)
print("-------afterReshape------")
myMatrix[0][1] = 20
print("first=\n", myMatrix)
print("second=\n", MyThirdMatrix)

print(myMatrix.dtype)
print(MyThirdMatrix.dtype)

np.set_printoptions(linewidth = 200)
aMatrix = np.arange(1, 10, 0.5)
print(aMatrix)
# 包含起点和终点
bMatrix = np.linspace(1, 10, 10)
print(bMatrix)

cMatrix = np.linspace(1, 10, 10, endpoint = False)
print(cMatrix)

# 指数函数数值，10一次方至2次方9个数
print("----logSpace-----")
dMatrix = np.logspace(1, 2, 9, endpoint = True, base = 10)
print(dMatrix)

# ask码转换
s = 'abcd'
gMatrix = np.fromstring(s, dtype = np.int8)
print(gMatrix)

print("------2baseLog-----")
twoMatrix = np.logspace(0, 9, 10, base = 2)
print(twoMatrix)
i = np.arange(0, 10, 2)
print(i)
two = twoMatrix[i]
print(two)
print(twoMatrix)

print("--randomNum-----")
randomMatrix = np.random.rand(10)
print(randomMatrix)
print(randomMatrix > 0.5)
largerMatrix = randomMatrix[randomMatrix > 0.5]
print("largerMatrix:", largerMatrix)
randomMatrix[randomMatrix > 0.5] = 0.5
print(randomMatrix)

print("------matrixTransfer------")
transMatrix = np.arange(0, 60, 10)
print("transMatrix:", transMatrix)
reshapeTransMatrix = transMatrix.reshape((-1, 1))
print(reshapeTransMatrix)
columeMatrix = np.arange(6)
print(columeMatrix)
addMatrix = reshapeTransMatrix + columeMatrix
print(addMatrix)

print("-------去重------")
uniqueArray = np.array((1, 2, 3, 4, 5, 6, 6, 3, 6, 7, 7, 8))
print(np.unique(uniqueArray))
uniqueDoubleArray = np.array(((1, 2), (2, 3), (2, 3), (4, 5)))
print(np.unique(uniqueDoubleArray))
print("-----二维去重-------")
print(np.array(list(set([tuple(t) for t in uniqueDoubleArray]))))

print("------数组转置-------")
reshapeArrayOne = np.arange(1, 10).reshape((3, 3))
reshapeArrayTwo = np.arange(11, 20).reshape((3, 3))
reshapeArrayThree = np.arange(101, 110).reshape((3, 3))
print('reshapeArrayOne=\n', reshapeArrayOne)
print('reshapeArrayTwo=\n', reshapeArrayTwo)
print('reshapeArrayThree=\n', reshapeArrayThree)
print('axis=0\n', np.stack((reshapeArrayOne, reshapeArrayTwo, reshapeArrayThree), axis = 0))
print('axis=1\n', np.stack((reshapeArrayOne, reshapeArrayTwo, reshapeArrayThree), axis = 1))
print('axis=2\n', np.stack((reshapeArrayOne, reshapeArrayTwo, reshapeArrayThree), axis = 2))

multiArr = np.arange(1, 10).reshape(3, 3)
print(multiArr)
multiArrayed = multiArr + 10
print(multiArrayed)
print(np.dot(multiArr, multiArrayed))
print(multiArr * multiArrayed)

print("----正态分布")
mu = 0
sigma = 1
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 51)
y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi))
print('x.shape:', x.shape)
print('x=\n', x)
print('y.shape:', y.shape)
print('y.shape:', y.shape)
print('y=\n', y)
plt.figure(facecolor = 'w')
plt.plot(x, y, 'r-', x, y, 'go', linewidth = 2, markersize = 8)
plt.xlabel('X', fontsize = 15)
plt.ylabel('Y', fontsize = 15)
plt.title('Gauss Distribution', fontsize = 18)
plt.grid(True)
plt.show()

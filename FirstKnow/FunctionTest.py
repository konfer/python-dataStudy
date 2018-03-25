# coding:utf-8

def sum(x, y):
	return x + y


a = sum(1, 2)
print (a)


def f(a, b, c):
	return a + b + c


print (f(1, 2, 3))

print ("------")


def func(s, count):
	if count > 10:
		print (s)
	else:
		print ("not right")


func("show it ", 1)

a = func


# 函数式编程

def p(msg):
	print (msg)


p('hello world')
f = p
f('hello world second time')


def renturnTest():
	return 1, 2, 3


r = renturnTest()
print (type(r))
print (r)
u, v, w = renturnTest()

print ("divided print ----")
print (w, u, v)


def g():
	"""
		this is the first string
    """


print (g.__doc__)
g.count = 1
print (g.count)


def f(name, count = 1, *args, **kwargs):
	print ("name=", name)
	print ("count=", count)
	print ("args=", args)
	print ("kwargs=", kwargs)


print("-------first-------")
f(count = 11, name = "python")
print("-------second-------")
f("python", 11)
# 需严格与函数定义顺序一致
f("python", 12, 13, 14, 15, code = "java", num = 15)

a = lambda x: x + 1 if x > 10 else x - 10
print (a(1))

dx = 1

def f():
	x = 2
	print (x)


f()

print ("----f_bag------")


def f_bag(x):
	def myf2(y):
		return x + y
	
	return myf2


myf2 = f_bag(5)
print (myf2(10))


# 闭包

def start(name):
	def wrapper(f):
		def wrapperInside():
			print ('start by ', name)
			f()
		
		return wrapperInside
	
	return wrapper


@start("jordan")
def f():
	print ("Function")


# 函数作为参数
# 函数作为参数b
def sum(x, y, p = None):
	s = x + y
	if p:
		p(s)
	return s


sum(100, 200)


# sum(100, 200,print())

def do_sum(data, method):
	return method(data)


def getTwoSumNum(numbers,target):
	l=[]
	for i in range(len(numbers)-1):
		for j in range(i+1,len(numbers)):
			if numbers[i]+numbers[j]==target:
				l.append([numbers[i],numbers[j]])
	if l:
		return l
	else:
		return "no value"
print ("two sum")
	
print (getTwoSumNum([1,2,3,4] ,5))
print (getTwoSumNum([1,2,3,4],8))


print("--------")
f=abs
def add(x,y,f):
	return f(x)+f(y)

print(add(-5,6,f))

print("-----reduce-------")

from functools import reduce

l=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l))
print(reduce(lambda x,y:x+y,l,10)) #lambda最后一个参数作为x的初始值

print("-------map---------")

l=[1,2,3,4,6,7]
new_list=list(map(lambda i:i+1,l))
print(new_list)

print("--filterg---")
filterList=list(filter(lambda x:x>2,l))
print(filterList)

print("------wrap-------")

def hello(fn):
	def wrapper():
#		print(dir(fnb))
		print("hello, %s"%fn.__name__)
#		fn()
		print("goodbye,%s" % fn.__name__)
	return wrapper


@hello
def foo():
	print("i am foo")

foo()

print("-----doubleWrap-------")

def makeHtmlTag(tag,*args,**kwds):
	def real_decorator(fn):
		css_class="class='[0]'", format(kwds["css_class"])\
			if "css_class" in kwds else ""
		def wrapped(*args,**kwds):
			str1="<"+tag+str(css_class)+">"+fn(*args,**kwds)+"</"+tag+">"
			return str1
		return wrapped
	return real_decorator

@makeHtmlTag(tag="b",css_class = "hold_css")
@makeHtmlTag(tag="i",css_class = "italic_css")
def helloWorld():
	return "Hello World"

print(helloWorld())

def inc(x):
	def incx(y):
		return x+y
	return incx

inc2=inc(2)
inc5=inc(5)

print(inc2(8))
print(inc5(8))

name_len=map(len,['qi','yue','July'])
print(name_len)
for str in name_len:
	print(str)
	
myNum=[2,-5,9,7,-2,5,3,1,0,-3,8]
positive_num_cnt=0
positive_num_sum=0
for i in range(len(myNum)):
	if myNum[i]>0:
		positive_num_cnt+=1
		positive_num_sum+=myNum[i]
		
if positive_num_cnt>0:
	average=positive_num_sum/positive_num_cnt
	
print(average)
print(myNum)

def add(x,y):
	return x+y

myNumFilterList=list(filter(lambda x:x>0,myNum))
for _num in myNumFilterList:
	print(_num)

print("--------averageFunctionTest---")
average=reduce(add,myNumFilterList)/len(myNumFilterList)
print(average)













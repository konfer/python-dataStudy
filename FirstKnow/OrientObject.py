# coding:utf-8

import sys
from FirstKnow import FunctionTest

class A(object):
	def __init__(self,_id):
		self.id=_id
		print ('A')

print (type(A))


class B(object):
	def __init__(self):
		pass
	def func(self):
		print ('func')
	
	def func2(self, msg):
		print (msg)
	
print ("------dir-------")
print (dir(B))
print ("-------dict----------")
print (B.__dict__)


class C(A):
	pass

class D(A):
	def __init__(self,_id):
	#	super(B, self).__init__(_id)
		print  (_id)

c=C(1)
d=D(1)


b = B()

b.func()
b.func2("python")


class bookAuthor(object):
	author = "Guide"  # 类变量
	
	def __init__(self, page):
		self.page = page  # 实例变量
	
	@classmethod
	def class_method(selfcls, msg):
		return msg
	
	@staticmethod
	def static_method(msg):
		return msg


book_a = bookAuthor(10)
book_b = bookAuthor(200)

print (book_a.author)
print (book_b.author)

book_b.author = "python"  # 赋值予实例变量

print (book_a.page)
print (book_b.page)

print (book_b.author ) # 先查找实例变量，再查找类变量

print (bookAuthor.class_method("classmethod called"))
print (bookAuthor.static_method("staticmethod called"))

print(dir("ABC"))

class Student(object):
	school='high'
	
	def __init__(self,name,age,level='l'):
		self.__name=name
		self.__age=age
		self.level=level
		
	def detail(self):
		print(self.__name+":"+str(self.__age))
		
	def setName(self,name):
		self.__name=name
		
	def setAge(self,age):
		self.__age=age
	
	def get_name(self):
		return self.__name
	
	def get_age(self):
		return self.__age

lilei=Student('lilei',20)
lilei.detail()
lilei.setAge(15)
print(lilei.get_age())
print(dir(lilei))
print(hasattr(lilei,'name'))
print(hasattr(lilei,'level')) #仅仅针对公共变量
setattr(lilei,'level','m')
print (lilei.level)
print(getattr(lilei,'level'))
getDetail=getattr(lilei,'detail')
getDetail()
print(sys.path)


import traceback

from types import MethodType

class MyClass(object):
	__slots__=['name','set_name'] #限制属性

def set_name(self,name):
	self.name=name
	
cls=MyClass()
cls.name='Tom'
cls.set_name=MethodType(set_name,cls)
cls.set_name('Jerry')

try:
	cls.age=30
except AttributeError:
	traceback.print_exc()
	
class Student(object):
	
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('not int')
		
		elif (value<0) or (value>100):
			raise ValueError('not between 0~100')
		
		self._score=value
		
	@property
	def double_score(self):
		return self._score*2
		
s=Student()
s.score=75
print(s.score)
	
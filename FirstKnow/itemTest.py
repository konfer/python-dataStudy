#coding:utf-8

class Fib100:
	def __init__(self):
		self.one,self.sec=0,1
		
	def __iter__(self):
		return self
	
	def __next__(self):
		self.one,self.sec=self.sec,self.one+self.sec
		if self.one>100:
			raise StopIteration()
		return self.one,self.sec
		
for i in Fib100():
	print(i)
	
	
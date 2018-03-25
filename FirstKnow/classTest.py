# coding:utf-8

class A:
	def __init__ (self, number):
		self.number = number


class B (A):
	pass


#b = B ()
a = A (10)

print (a.number)

# coding:utf-8

print (id (1))


def f ():
	pass


print (id (f))
fa = f
print (id (fa))

del fa
del f


class A:
	pass


a = 10
b = 10

print (id (a))
print (id (b))

a1 = A ()
a2 = A ()

print (a is b)
print (a1 is a2)

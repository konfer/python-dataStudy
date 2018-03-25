# coding:utf-8

from  collections import Iterable
from  collections import Iterator


print(isinstance([1, 2, 3], Iterable))  # 判断是否可迭代
print(isinstance((), Iterable))
print(isinstance(123, Iterable))
print(isinstance('a,b,c', Iterable))

g = (x * x for x in range(10))
print(type(g))
print(isinstance(g, Iterable))

g = (x * x for x in range(10))
print(type(g))
print((isinstance(g, Iterable)))


def fib(limit):
	n, a, b = 0, 0, 1
	while n < limit:
		yield b
		a, b = b, a + b
		n += 1
	return 'done'
	return 'done'


for i in g:
	print(i)

f = fib(6)
print(type(f))
print(isinstance(f, Iterable))
print(isinstance(f, Iterator))

print("-----iter-------")

for x in f:
	print(x)

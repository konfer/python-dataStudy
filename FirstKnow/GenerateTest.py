#coding:utf-8

#平方表

square_tables=[]

for i in range(10000):
	square_tables.append(i*i)
for i in range(10):
	print (square_tables[i])
	
square_generator=(x*x for x in range(50000))

print("------generator----")
for i in range(10):
	print(next(square_generator))
	
print("-------generatorTest--------")

def fib(limit):
	n, a, b = 0, 0, 1
	while n<limit:
		yield b
		a,b=b,a+b
		n+=1
	return 'done'

f=fib(5)
print(type(f))
print(next(f))
print(next(f))
print(next(f))


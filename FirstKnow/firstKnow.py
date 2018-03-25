print ("hello world")

a = 3
b = 10000000
c = 1.2

e = True
f = False
g = e and f
h = not True

print (a)
print (e)
print (f)

print (h)

print (ord ('A'))
print (chr (66))

print (3 ** 2)
print (3 * 2)
print (3 % 2)
print (a == 5)
print (a != 5)
print (a in [1, 2, 5])

print (True and False)

mySum = 0
for i in range (100):
	mySum = mySum + 1 + i
print (mySum)

for myNumber in range (1, 10, 2):
	print (myNumber)

secondSum = 0
for i in range (100):
	secondSum = secondSum + i + 1
	if i == 2:
		continue
	elif i == 80:
		break
print (secondSum)

print ("---if test---")

number = 9

print ("if test b")

if number > 10:
	print ("big number")
elif number > 5 and number <= 10:
	print ("medium")
else:
	print ("small")

print ("----while test------")

while number > 0:
	print (number)
	number -= 1

print (" ")
print ("---for else test-------")
for i in range (1, 10):
	if i % 2 == 0:
		print (i)
	else:
		#		break
		continue
else:
	print ("normal Exit")

l=[1,2,3,4,5]
for index,text in enumerate(l):
	print(index,text)
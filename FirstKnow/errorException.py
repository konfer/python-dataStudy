# coding:utf-8

try:
	r = 10 / 0
except:
	ZeroDivisionError
	print("got it")
else:
	print("no error")
finally:
	print("end")

print("-----------")

d = {"name": 1}

try:
	#	d ["n"]
	d ["name"]
except KeyError:
	print ("The key is not ready")
else:
	print ("no error")

#coding:utf-8

import json

file1=open('fileTest.txt')
file2=open("outPutTestb.txt","w")
#w为全部重写，a(append)为部分重写

while True:
	line=file1.readline()
	file2.write('"'+line+"',")
	if not line:
		break

file3 = open("outPuttest.txt", "w")
for line in open("fileTest.txt"):
	file2.write('"'+line+'"')
	
with open("fileTest.txt",'r') as f:
	data = f.read()
	
#自带文本关闭功能
with open("fileTest.txt",'r') as f:
	data=f.read()


file1.close()
file2.close()

#json
d1=dict(name='小王',age=20,score=80)
str=json.dumps(d1)
print(str)
d2=json.loads(str)
print (type(d2))

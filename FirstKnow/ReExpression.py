# coding:utf-8

import re

m = re.match(r'dog', 'dog cat dog')
print(m.group())
print(re.match(r'cat', 'dog cat dog'))
s = re.search(r'cat', 'dog cat dog')
print(s.group())
print(re.findall(r'dog', 'dog cat dog'))

contactInfo = 'Doe,John:555-1222'
c = re.search(r'(\w+),(\w+):(\S+)', contactInfo)
for i in range(3):
	print(c.group(i))
	
#print(m.group(2))
#print(m.group(3))

str='purple alice-b@google.com monkey dishwasher'
match=re.search(r'\w+@\w+',str)
if match:
	print(match.group())
	
matchCompleteEmailAddress=re.search(r'[\w.-]+@[\w.-]+',str)
if matchCompleteEmailAddress:
	print(matchCompleteEmailAddress.group())
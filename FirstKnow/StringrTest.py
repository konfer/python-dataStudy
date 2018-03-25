# coding:utf-8

import string

s = 'abc'
# s[0]='c '不能被修改b

s = ' sfdf fdfd '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.rsplit())
print(s)

# 大小写

s = 'adsa dfe'
s2 = 'adt'
print(s.upper())
print(s.upper().lower())
print(s.capitalize())  # 首字母大写

# 位置
print (s.index('df'))

try:
	print (s.index('go'))
except ValueError:
	print("no value")
	pass  # python3中 cmp被移除bb

print(s == s2)
print(s < s2)
print(s > s2)

print('----------')
print(len(s))
s1 = ''
if s is None:
	print('none')
elif s==False:
	print("Empty")

#分割和连接

s3='abc,def,ghi'
spliiter=s.split(',')
print(type(spliiter))
print(spliiter)

s4="""abc
def
ghib
efg

"""
print('----------')

s_4=s4.split('\n')
s_5=s4.splitlines()
print (s_4)
print (s_5)

print(''.join(s_4))

#常用判断

print('----------')
s5='abcdfef'
print(s5.startswith('a'))
print (s5.endswith('fef'))
print('12345abcd'.isalnum()) #检查是否由字母和数字组成
print('\t12ab'.isalnum())
print('abcd'.isalpha())
print('1234'.isdigit())
print('  '.isspace())
print('ABCD1234'.islower())
print ('abcde12345'.isupper())
print('Hello world'.istitle()) #单词首字母大写

print('----------')
#字符串到数字
print(str(5))
print(float('123434.45'))
print(int('123'))

print(int('777',16))
print (int('777',8))

s6='dfsdfds'
l=list(s6)
print(l[3])

print('----------')
#none的判断
x=None
if not x:
	print ('none')
else:
	print ('not none')
























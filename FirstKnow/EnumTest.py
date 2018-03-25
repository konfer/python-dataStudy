#coding:utf-8

from enum import Enum

Month=Enum('Month',('Jan','Feb','Mar','Apr'))

print(Month.__members__)

for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
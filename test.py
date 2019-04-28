#!/usr/bin/python3
# _*_coding: UTF-8 _*_
'a test module'
__author__='wjj'

from enum import Enum

Month=Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
# coding=gb2312
# -*- coding: gb2312 -*-
import argparse
import sys
import re

file_name = 'xxx'


#if no argv use file
if len(sys.argv) == 2:
	file_name = sys.argv[1]

file_object = open(file_name,'r+')

try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

# print(all_the_text)
def strToDoubleStr(matched):
    intStr = matched.group("number")
    print(intStr)
    resultStr = int(intStr.replace('px',''))*2
    print(resultStr)
    resultStr = 'unit('+str(resultStr)+'px)'
    return resultStr
    # print(intStr)
    # return addedValueStr;
    # return

all_the_text=re.sub(r'(?P<number>(\d+)px)',strToDoubleStr,all_the_text)


file_object.close()
file_object = open(file_name,'w+')

file_object.write(all_the_text)

file_object.close()
print(all_the_text)
print(file_name+'     success')

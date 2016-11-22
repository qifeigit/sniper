
# 将一个文本文件中的内容做替换，并且更新该文件
import argparse
import sys
import re

if len(sys.argv) == 1:
    sys.argv.append('--help')
parser = argparse.ArgumentParser()


file_object = open(sys.argv[1],'r+')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

# print(all_the_text)
all_the_text=re.sub(r'(\d+)px',"unit(\g<1>px)",all_the_text)

print(all_the_text)

file_object.close()
file_object = open(sys.argv[1],'w+')

file_object.write(all_the_text)


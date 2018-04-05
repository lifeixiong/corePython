# -*- coding:UTF-8 -*-

'''
1-2 匹配由单个空格分隔的任意单词对， 也就是名和姓。
'''
import re

pattern = "\w+\s\w+"

def check(name):
    print(name)
    m = re.match(pattern, name)
    if(m is not None):
        print("result", m)

check("H M")
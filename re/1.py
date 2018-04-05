# -*- coding:UTF-8 -*-

'''
1-1 识别后续的字符串： "bat"、"bit"、"but"、"hat"、"hit"或者"hut".
'''

import re

pattern = "[bh][aiu]t"
array = ["bat", "bit", "but", "hat", "hit", "hut"]
for item in array:
    m = re.match(pattern, item)
    if(m is not None):
        print(m.group())
#!/user/bin/env python3
# -*- coding: utf-8 -*-

import re

a = '明天|后天|hehe|两点水|阿西吧'

value = re.findall('明天', a)
print(value)

if len(value) > 0:
    print("a含有'明天'这个字符串")
else:
    print("a不含'明天'这个字符串")
#!/user/bin/env python3
# -*- coding: utf-8 -*-

import re

a = 'usv, uav,ubv,ucv,uwv,uzv,ucv,uov'

# 取u和v中间是abc中任意一个的字符串
findl = re.findall('u[abc]v', a)

print(findl)

# 用 ‘-’ 表示连续的字母
finda = re.findall('u[a-c]v', a)
print(finda)

# ‘^’ 符号放在前面表示取反
findb = re.findall('u[^a-c]v', a)
print(findb)

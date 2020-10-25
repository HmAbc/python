#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 数量词的词法是：{min,max} 。min 和 max 都是非负整数。如果逗号有而 max 被忽略了，则 max 没有限制。
# 如果逗号和 max 都被忽略了，则重复 min 次。
# 比如，\b[1-9][0-9]{3}\b,匹配的是 1000 ~ 9999 之间的数字( “\b” 表示单词边界），
# 而 \b[1-9][0-9]{2,4}\b，匹配的是一个在 100 ~ 99999 之间的数字。

import re

a = 'java*&39android##@@python'

# 数量词

findall = re.findall('[a-z]{4,7}', a)
print(findall)
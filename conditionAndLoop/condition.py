#!/user/bin/env python3
# -*- coding: utf-8 -*-

results = 89

if results > 90:
    print('优秀')
elif results > 80:
    print('良好')
elif results > 60:
    print('及格')
else :
    print('不及格')

java = 86
python = 68

if java > 80 and python > 80:
    print('优秀')
else :
    print('不优秀')

if (java >= 80 and java < 90) or (python >= 80 and python < 90):
    print('良好')

# if嵌套使用
print('\nif的嵌套使用')
if java > 80:
    if python > 80:
        print('优秀')
    else:
        print('不优秀')
else:
    print('不优秀')
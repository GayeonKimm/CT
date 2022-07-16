'''
맞았는데 더 빠른 방법은 없을까?

'''

import sys
input = sys.stdin.readline

s = input().strip()
temp = ''
for i in s:
    if i.isalpha():
        temp += i
k = input().strip()
if k in temp:
    print(1)
else:
    print(0)
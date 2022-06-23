'''
문자열 뒤에 A추가
뒤집고 뒤에 B추가 == 맨앞에 B추가
'''
import sys
input = sys.stdin.readline
s = list(map(str, input().strip()))
t = list(map(str, input().strip()))
print(s,t)

while len(s) != len(t):
    if t[-1] == 'B':
        t.pop()
        t = t[::-1] # reverse
    else:
        t.pop()
if s == t:
    print(1)
else:
    print(0)
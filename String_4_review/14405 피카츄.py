import sys
input = sys.stdin.readline

pocket = ['pi', 'ka', 'chu']
s = input().strip()
for i in pocket:
    if i in s:
        s = s.replace(i, '*') # 별로 대체 하는 방법쓰

chk = True
for i in s:
    if i != '*': # 아닌게있다면
        chk = False
        break

if chk:
    print("YES")
else:
    print("NO")
import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()

chk = False
for i in range(len(s)- len(p) + 1):
    if s[i:i+len(p)] == p:
        chk = True
        break
if chk:
    print(1)
else:
    print(0)
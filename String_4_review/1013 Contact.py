import sys
import re
input = sys.stdin.readline


n = int(input())
s = [input().strip() for _ in range(n)]

for i in s:
    p = re.compile("(100+1+|01)+")
    result = p.fullmatch(i)

    if result:
        print("YES")
    else:
        print("NO")
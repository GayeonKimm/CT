import re
import sys
input = sys.stdin.readline

N = int(input())
string = [input().strip() for _ in range(N)]

for i in string:
    p = re.compile("(100+1+|01)+")
    result = p.fullmatch(i)

    if result:
        print("YES")
    else:
        print("NO")

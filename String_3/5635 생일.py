'''
sort로 순서대로 정렬하는 방법 써먹어야지
근데 str로 저장되네 그러면 나눠서 append해야지

'''

import sys
input =sys.stdin.readline
n = int(input())
info = []

for _ in range(n):
    n, d, m, y = input().split()
    info.append([n, int(d), int(m), int(y)])
info.sort(key = lambda x: (x[3], x[2],x[1]))
print(info[-1][0])
print(info[0][0])
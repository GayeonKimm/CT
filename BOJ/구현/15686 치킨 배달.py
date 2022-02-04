import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

# 치킨집 탐방
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chicken.append([i, j])
        elif maps[i][j] == 1:
            home.append([i, j])
print("home = ", home)

# 치킨집 선택 리스트
pch = list(combinations(chicken, M))
print("pch = ", pch)
# 결과 저장할 리스트
result = [0] * len(pch)

for i in home:
    for j in range(len(pch)):
        a = 100
        for k in pch[j]:
            temp = abs(i[0]-k[0]) + abs(i[1]-k[1])
            a = min(a, temp)
            # print("i,j, k, a = ", i,j, k, a)
        result[j] += a

print(result)
print(min(result))

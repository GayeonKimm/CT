import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
maps = [[0] * n for _ in range(m)]
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            maps[i][j] = 1

visit = [[False]*n for _ in range(m)]

answer = []
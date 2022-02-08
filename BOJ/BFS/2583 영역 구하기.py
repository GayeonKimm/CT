# 일단 bfs

import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
maps = [[0] * n for _ in range(m)]
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            maps[i][j] = 1

def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    cnt = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if maps[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    cnt += 1
                    q.append((nx,ny))
    return cnt

visit = [[False]*n for _ in range(m)]
answer = []
for i in range(m):
    for j in range(n):
        if maps[i][j] == 0 and not visit[i][j]:
            visit[i][j] = True
            count = bfs(i,j)
            answer.append(count)

print(len(answer))
answer.sort()
for i in answer:
    print(i, end = ' ')

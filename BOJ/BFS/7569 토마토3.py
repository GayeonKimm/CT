import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
maps = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

def bfs():
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,1,-1]

    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if maps[nz][nx][ny] == 0:
                    maps[nz][nx][ny] = maps[z][x][y] + 1
                    q.append((nz, nx,ny))

q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if maps[k][i][j] == 1:
                q.append((k,i,j))

bfs()
answer = 0
check = True
for i in maps:
    for j in i:
        for k in j:
            if k == 0:
                check = False
            answer = max(answer, k)

if check:
    print(answer-1)
else:
    print(-1)
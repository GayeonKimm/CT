import sys
input = sys.stdin.readline

import copy
from collections import deque

def bfs():
    global ans
    w = copy.deepcopy(maps)

    q = deque()
    # 바이러스 확장 코드
    for i in range(N):
        for j in range(M):
            if w[i][j] == 2:
                q.append((i,j))

    dx,dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append((nx,ny))

    # 안전구역 세는 코드 ans에 저장
    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)

def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall(x+1)
                maps[i][j] = 0

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

ans = 0
wall(0)
print(ans)
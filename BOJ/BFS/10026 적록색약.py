# 적록 색약은 R-G구별 못함
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
maps = [list(input().strip()) for _ in range(N)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx<N and 0<= ny <N:
                if maps[nx][ny] == maps[x][y] and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx,ny))


answer = []

# 일반 사람 버전
visit = [[False]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            bfs(i,j)
            cnt += 1
answer.append(cnt)

# 색약 버전
visit = [[False]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if maps[i][j] == 'R':
            maps[i][j] = 'G'
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            bfs(i,j)
            cnt += 1
answer.append(cnt)
print(answer)
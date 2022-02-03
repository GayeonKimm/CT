# 이 문제는 1인 것들을 미리 담아놓고 bfs를 수행해야 하는 문제임!!!

import sys
input = sys.stdin.readline

c, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]

from collections import deque
q = deque()
for i in range(r):
    for j in range(c):
        if maps[i][j] == 1:
            q.append((i,j))

def bfs():
    dx,dy = [1,-1,0,0], [0,0,-1,1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))

bfs()
# 0이 존재하는지 아닌지 판별
check = True
answer = 0
for i in maps:
    for j in i:
        if j == 0:
            check = False
        answer = max(answer, j)

# 0 존재하지 않은 True면 answer-1 리턴
if check:
    print(answer-1)
else:
    print(-1)
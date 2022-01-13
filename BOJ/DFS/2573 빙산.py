import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
check = False
day = 0

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] and chk[nx][ny]==False:
                    chk[nx][ny]=True
                    q.append((nx,ny))
                elif maps[nx][ny]==0:
                    count[x][y] += 1
    return 1

while True:
    chk = [[False] * m for _ in range(n)] # 이거 while 밖에 쓰면 틀렸다고 함
    count = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] and chk[i][j]==False:
                chk[i][j]=True
                result.append((bfs(i,j)))

    for i in range(n):
        for j in range(m):
            maps[i][j] -= count[i][j]
            if maps[i][j] < 0:
                maps[i][j]=0

    if len(result)==0:
        break
    if len(result) >= 2:
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)

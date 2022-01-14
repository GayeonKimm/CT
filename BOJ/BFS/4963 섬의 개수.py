import sys
input = sys.stdin.readline
from collections import deque
# 대각선을 어떻게 찾지?!! idea

def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx = [-1,1,0,0, 1,-1,1,-1]
    dy = [0,0,-1,1, -1,-1,1,1]
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if maps[nx][ny] and chk[nx][ny]==False:
                    chk[nx][ny]=True
                    q.append((nx,ny))

while True:
    w,h = map(int, input().split())
    if w==0 and h==0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    chk = [[False]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] and chk[i][j]==False:
                chk[i][j] = True
                bfs(i,j)
                cnt += 1
    print(cnt)
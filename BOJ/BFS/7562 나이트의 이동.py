import sys
input = sys.stdin.readline

from collections import deque
def bfs():
    q = deque()
    q.append((sx, sy))
    maps[sx][sy] = 1

    dx = [-2,-1,1,2, -2,-1,1,2]
    dy = [1,2,2,1, -1,-2,-2,-1]
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            return maps[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))

t = int(input())
for _ in range(t):
    n = int(input())
    maps = [[0]*n for _ in range(n)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs())
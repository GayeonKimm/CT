# dfs
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# dfs는 컴파일 에러가 남

m, n, k = map(int, input().split())
maps = [[0] * n for _ in range(m)]
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            maps[i][j] = 1

def dfs(x,y):
    global cnt
    cnt += 1
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx < m and 0<=ny<n:
            if maps[nx][ny] == 0 and not visit[nx][ny]:
                visit[nx][ny] = True
                dfs(nx,ny)
    return cnt

visit = [[False]*n for _ in range(m)]
answer = []
for i in range(m):
    for j in range(n):
        if maps[i][j] == 0 and not visit[i][j]:
            visit[i][j] = True
            cnt = 0
            answer.append(dfs(i,j))

print(len(answer))
answer.sort()
for i in answer:
    print(i, end = ' ')
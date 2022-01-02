import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chk = [[False]*M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))




for i in range(N):
    for j in range(M):
        if graph[i][j]== 2 and chk[i][j]==False:
            chk[i][j]=True
            bfs(i,j)


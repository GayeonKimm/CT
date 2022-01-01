from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
chk =[[False]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상 하 좌 우

chk[0][0] = True
def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] and chk[nx][ny]==False:
                    chk[nx][ny]=True
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
    print(graph)

    return graph[N-1][M-1]

print(bfs(0,0))



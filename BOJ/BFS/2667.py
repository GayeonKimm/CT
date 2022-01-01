# 단지 번호 붙이기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x,y))
    cnt = 1
    # global cnt
    # cnt += 1

    while q:
        x, y = q.popleft()
        for a in range(4):
            nx = x+ dx[a]
            ny = y+ dy[a]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] and chk[nx][ny]==False:
                    chk[nx][ny]=True
                    q.append((nx,ny))
                    cnt += 1
    town_list.append(cnt)


N = int(input())
graph =[list(map(int, input().strip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]
town = 0
town_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] and chk[i][j]==False:
            chk[i][j]=True
            # cnt = 0
            bfs(i,j)
            town += 1
town_list.sort()
print(town)
# print("\n".join(town_list))
# 숫자잖아..
for i in town_list:
    print(i)

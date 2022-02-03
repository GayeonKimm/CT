import sys
input = sys.stdin.readline

from collections import deque

def bfs(x,y,k):
    q = deque()
    q.append((x,y))

    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] > k and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))


# maps의 최대값 설정해두는 코드
N = int(input())
maps = []
max_value = 0
for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(N):
        if maps[i][j] > max_value:
            max_value = maps[i][j]


# max 보다 크면 섬으로 인정해줄게
answer = []
for k in range(max_value):
    visit = [[False]*N for _ in range(N)]
    seom = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > k and not visit[i][j]:
                visit[i][j] = True
                bfs(i, j, k)
                seom += 1
    answer.append(seom)
# k이상인 것들을 하나씩 다 돌고와서 answer에 append해야됨

print(answer)
print(max(answer))
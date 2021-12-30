# 유기농 배추
# chk 만들어서 하는 방법이라 아래 method보단 시간 조금 더 소요

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(x, y):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and chk[nx][ny]==False:
                chk[nx][ny] = True
                dfs(nx, ny)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    chk = [[False] * m for _ in range(n)]
    answer = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and chk[i][j]==False:
                chk[i][j] = True
                dfs(i, j)
                answer += 1
    print(answer)


# chk 사용 안하는 방식

# import sys
# input = sys.stdin.readline
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
# def dfs(x,y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (0 <= nx < N) and (0 <= ny < M):
#             if matrix[nx][ny] == 1:
#                 matrix[nx][ny] = -1
#                 dfs(nx, ny)
#
# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     matrix = [[0]*M for _ in range(N)]
#     chk = [[False]*M for _ in range(N)]
#     answer = 0
#
#     for _ in range(K):
#         a, b = map(int, input().split())
#         matrix[b][a] = 1
#
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] > 0:
#                 dfs(i, j)
#                 answer += 1
#     print(answer)





# 연결 요소의 개수

# import sys
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# graph = [[]*(N+1) for _ in range(N+1)]
# chk = [False]*(N+1)
#
# for _ in range(M):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def dfs(i):
#     chk[i]=True
#     for a in graph[i]:
#         if chk[a]==False:
#             dfs(a)
#
# answer = 0
# for i in range(N):
#     if graph[i] and chk[i]==False:
#         dfs(i)
#         answer += 1
#         # print(i, "answer = ", answer)
#
# print(answer)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(i):
    chk[i]=True
    for a in graph[i]:
        if chk[a]==False:
            dfs(a)

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
chk = [False]*(N+1)
answer = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if chk[i]==False:
        dfs(i)
        answer += 1

print(answer)
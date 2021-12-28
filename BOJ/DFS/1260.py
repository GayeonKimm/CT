# 1260 DFS와 BFS
import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visit1[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(n+1):
            if visit1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit1[i] =1
def dfs(v):
    visit2[v] = 1
    print(v, end=" ")
    for i in range(n+1):
        if visit2[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visit1 = [0] * (n+1)
visit2 = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
print(graph)

dfs(v)
print() # 띄어쓰기 역할
bfs(v)
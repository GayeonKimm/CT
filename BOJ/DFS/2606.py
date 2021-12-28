# 2606 바이러스
# 살짝만 다르게 풀었음

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] * (n+1) for _ in range(n+1)]
print(graph)

cnt = 0
chk = [False] * (n+1)
print(chk)

def dfs(start):
    global cnt
    chk[start] = True
    for i in graph[start]:
        if chk[i]==False:
            dfs(i)
            cnt += 1

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
dfs(1)
print(cnt)
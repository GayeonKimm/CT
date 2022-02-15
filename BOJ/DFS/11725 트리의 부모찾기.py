import sys
input = sys.stdin.readline

def dfs(x):
    for i in maps[x]:
        if answer[i] == 0:
            answer[i] = x
            dfs(i)

N = int(input())
maps = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

dfs(1)
for i in answer[2:]:
    print(i)

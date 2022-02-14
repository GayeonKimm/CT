import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        nx = q.popleft()
        for i in maps[nx]:
            if answer[i] == 0:
                answer[i] = nx
                q.append(i)
                # 그 다음게 들어가야지

N = int(input())
maps = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)
# print(maps)
bfs(1)
print(answer)
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return visit[x]
        for i in (x-1, x+1, 2*x):
            #if <= MAX 안했다가 계속 틀림
            if 0 <= i <= MAX and not visit[i]:
                visit[i] = visit[x] + 1
                q.append(i)

n, k = map(int,input().split())
MAX = 100000
visit = [0] * (MAX+1)
print(bfs(n))

# def bfs(n):
#     q = deque()
#     q.append(n)
#     while q:
#         x = q.popleft()
#         if x == k:
#             print(visit[x])
#             break
#         for i in (x-1, x+1, 2*x):
#             if 0 <= i < MAX and not visit[i]:
#                 visit[i] = visit[x] + 1
#                 q.append(i)
#
# bfs(n)



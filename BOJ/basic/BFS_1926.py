"""
BFS
1. 아이디어
- 2중 for문

2. 시간 복잡도
- BFS : O(V+E)
- V : 500*500
- E : 4*500*500
100만. <2억

3. 자료구조
- 그래프 전체 지도 int[][] : 2차원 배열
- 방문 : bool[][] : 2차원 배열
- Queue(BFS)
"""

from collections import deque

import sys
input = sys.stdin.readline

n,m = map (int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1   # 그림의 사이즈
    q = deque()
    q.append((y,x))

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            # 사이즈 넘어가지 않도록
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs
# 전체 크기 리턴

cnt = 0  # 전체
maxv = 0  # maximum value

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 그림갯수로 올리고
            # bfs 를 통해 그림의 크기를 구해주기
            cnt += 1
            maxv = max(maxv, bfs(j,i))


print(cnt)
print(maxv)


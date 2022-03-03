# 재풀이. +7

from collections import deque
def solution(maps):
    q = deque()
    q.append((0, 0))

    # 5*5 고정이 아니라서 해야되겟더라고
    n = len(maps)
    m = len(maps[0])

    graph = [[-1] * m for _ in range(n)]
    chk = [[False] * m for _ in range(n)]
    graph[0][0] = 1
    chk[0][0] = True

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and chk[nx][ny] == False:
                    if graph[nx][ny] == -1:
                        chk[nx][ny] = True
                        graph[nx][ny] = graph[x][y] + 1
                        q.append((nx, ny))

    return graph[-1][-1]

print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,1],
                [0,0,0,0,1]]))

from collections import deque
def solution(maps):
    r = len(maps)
    c = len(maps[0])

    table = [[-1 for _ in range(c)] for _ in range(r)]
    q = deque()
    q.append((0, 0))

    table[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny]:
                    if table[nx][ny] == -1:
                        table[nx][ny] = table[x][y] + 1
                        q.append((nx, ny))

    answer = table[-1][-1]
    return answer

print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,1],
                [0,0,0,0,1]]))

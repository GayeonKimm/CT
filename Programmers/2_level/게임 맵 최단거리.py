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
                # 이 범위가 이상했어서 오류 났는데 이렇게 쓴게 맞음!
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

# [[1, -1, 9, 10, 2],
#  [2, -1, 8, -1, 3],
#  [3, -1, 7, 8, 4],
#  [4, 5, 6, -1, 5],
# [-1, -1, -1, -1, 3]]

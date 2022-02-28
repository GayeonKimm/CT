from collections import deque
def bfs(place, i, j):
    visit = [[False] * 5 for i in range(5)]
    visit[i][j] = True

    q = deque()
    q.append((i,j,0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, dist = q.popleft()

        if 0 < dist < 3 and place[x][y] == 'P':
            return False

        if dist > 2:
            break

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            nd = dist + 1

            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] != 'X' and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    q.append((nx, ny, nd))
    return True


def solution(places):
    answer = []

    for place in places:
        chk = False

        for i in range(5):           # len(place)
            for j in range(5):      # len(place[0])
                if place[i][j] == 'P':
                    if not bfs(place, i, j):       # False면
                        answer.append(0)
                        chk = True
                        break
                        # 하나라도 거리두기 지켜지지 않으면 확인할 필요 없음

            if chk:    #chk가 1이면
                break
        else:
            answer.append(1)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
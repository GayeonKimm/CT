# 백트래킹
# 알파벳 다음거있으면 이동, 아니면 다시 그 알파벳 전 글자로 돌아가서 확인해야됨
# 이러면 ord가 아니라 리스트 재탐색으로 가야하는게 아닐까?

# 간단하게 00에서 시작해서 마지막까지 가는데, 중간에 재탐색 기회를 주는 문제로

from collections import deque
def bfs(maps):
    q = deque()
    q.append((0,0,1))
    visit = [[[0]*2 for _ in range(5)] for _ in range(5)]
    visit[0][0][1] = 1
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x, y, w = q.popleft()
        if x == 4 and y == 4:
            return visit[4][4]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<5 and 0<=ny<5:
                if maps[nx][ny] == chr(ord(maps[x][y])+1) and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append((nx, ny, w))
                elif maps[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append((nx,ny,0))

            # 진짜 모르겠다
    return visit[4][4]

def solution():
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z']
    alpha.index(i)+1
    return


maps = [['A', 'B', 'T', 'T', 'T'],
        ['T', 'C', 'D', 'E', 'T'],
        ['T', 'T', 'T', 'F', 'T'],
        ['B', 'A', 'H', 'G', 'T'],
        ['C', 'D', 'E', 'F', 'G']]
print(solution())
# 15
import sys
input = sys.stdin.readline
from collections import deque

def solution():
    q = deque()
    # 안뚤린 벽 저장
    q.append((0, 0, 1))
    # visit에 저장
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1 # 벽을 한번 부술 수 있는 상태에서 시작

    dx,dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x, y, w = q.popleft()
        # 마지막 위치에 도착했다면 출력
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만나고 벽을 한 번 부술수 있는 경우
                if maps[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append((nx,ny,0))
                # 벽이 없고 방문한 적 없는 경우
                elif maps[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append((nx,ny,w))

    return -1

n,m = map(int, input().split())
maps = [list(map(int,input().strip())) for _ in range(n)]
print(solution())

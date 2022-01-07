# bfs문제

from collections import deque
def solution(maps):
    r = len(maps)
    c = len(maps[0])

    # chk 겸 작성하는 리스트
    # 벽이 있으면 -1 을 출력하기 위함임!
    graph = [[-1 for _ in range(c)] for _ in range(r)]
    q = deque()
    q.append((0,0))
    graph[0][0]=1
    # 시작값은 1로 해야 더하니까

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx<r and 0<=ny<c:
                if maps[nx][ny] and graph[nx][ny]==-1:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx,ny))

    answer = graph[-1][-1]

    return answer

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))
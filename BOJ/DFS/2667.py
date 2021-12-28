# 2667 단지 번호 붙이기
import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(x,y):
    global each
    each += 1

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[nx][ny] == 1 and chk[nx][ny]==False:
                chk[nx][ny] = True
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and chk[i][j]==False:
            chk[i][j]=True
            each = 0
            dfs(i,j)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)

# print("\n".join(result)) #리스트지만 숫자여서 오류남 ~~
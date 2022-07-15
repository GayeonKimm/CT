'''
어떻게 교환할 두개를 찾느냐가 포인트
'''
import sys
input = sys.stdin.readline

def check(maps):
    answer = 1
    for i in range(n):
        # 행 check
        cnt = 1
        for j in range(n-1):
            if maps[i][j] == maps[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
        # 열 check
        cnt = 1
        for j in range(n-1):
            if maps[j][i] == maps[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
    return answer

# main
n = int(input())
arr = [list(input().strip()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # 열바꾸기
        if j+1 < n:
            arr[i][j],arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = check(arr)
            if temp > answer:
                answer = temp
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]

        # 행바꾸기
        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = check(arr)
            if temp > answer:
                answer = temp
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(answer)

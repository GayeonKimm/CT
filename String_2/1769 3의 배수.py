import sys
input = sys.stdin.readline

x = input().strip()
cnt = 0

def solution(x, cnt):
    if len(x) > 1:
        cnt += 1
        t = 0
        for i in x:
            t += int(i)
        solution(str(t), cnt)
    else:
        if int(x) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")

solution(x, cnt)
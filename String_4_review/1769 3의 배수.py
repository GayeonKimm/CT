'''
반복하는 부분이 어렵네....
'''
import sys
input = sys.stdin.readline

x = input().strip()
cnt = 0
while len(x) > 1:
    y = 0
    cnt += 1
    for i in x:
        y += int(i)
        x = str(y)
print(cnt)
if int(x) % 3 == 0:   # 여기 y로 하면 안되는 거네 .... 네임에러 남
    print("YES")
else:
    print("NO")


# 다른 방법
# 함수 계속 돌리면 됨
count = 0
def solution(x, count):
    if len(x) > 1:
        count += 1
        t = 0
        for i in x:
            t += int(i)
        solution(str(t), count)
    else:
        if int(x)%3 == 0:
            print(cnt)
            print('YES')
        else:
            print(cnt)
            print('NO')
print(solution(x, count))
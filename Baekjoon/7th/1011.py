# 시작과 끝은 1로 끝나야됨

t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    d = y-x
    cnt = 0
    move = 1
    move_p = 0
    while move_p < d:
        cnt += 1
        move_p += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)
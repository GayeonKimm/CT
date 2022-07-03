import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())

road = []
a = input().strip()
for i in a:
    road.insert(0, (i, '0'))
b = input().strip()
for i in b:
    road.append((i, '-1'))

t = int(input())
print(road)

# 이제 비교하자 자리 바꾸는 과정
for _ in range(t):
    # print(road)
    for i in range(len(road)-1):
        if road[i][1] == '0' and road[i+1][1] == '-1':
            road[i], road[i+1] = road[i+1], road[i]

            # 이게 계속 이동함 걍 미친듯이 이동
            # 선두 개미이면 반복을 멈춘다는게 뭔소리지?
            if road[i+1][0] == :
                break

answer = ''
for i in range(len(road)):
    answer += road[i][0]
print(answer)
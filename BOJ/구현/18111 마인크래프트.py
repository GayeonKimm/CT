'''
낮아서 채우면 개당 1점
높아서 깎으면 개당 2점

땅고르기 작업에 걸리는 최소 시간과 그 경우 땅의 높이 출력
b는 인벤토리에 있는 값
채워 넣어야 할 때 b값이 충분하지 않으면 안됨
= max_target 값이 b보다 크면 애초에 안됨
= max_target + b <= min_target 이면 안됨

pypy3로 제출
'''

import sys
input = sys.stdin.readline

n, m, b = map(int, input().strip().split())
maps = [list(map(int, input().strip().split())) for _ in range(n)]
answer = sys.maxsize # 초기값 임의로 설정
idx = 0

# 주어진 256층까지 다 해보기
for target in range(257):
    max_target, min_target = 0, 0
    for i in range(n):
        for j in range(m):
            # 높은 경우
            if maps[i][j] >= target:
                max_target += maps[i][j] - target
            # 낮은 경우
            else:
                min_target += target - maps[i][j]

    if max_target + b >= min_target:
        #  최소 시간 확인
        if min_target + (max_target*2) <= answer:
            answer = min_target + max_target*2
            idx = target
    else:
        break # 이거쓰면 시간은 좀 줄어듬, 연산 더 안해도 됨

print(answer, idx)

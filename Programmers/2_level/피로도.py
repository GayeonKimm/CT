'''
모든 경우의 수 확인해야하는 permutations
3으로 고정했었는데 꼭 dungeons len 처리해주고
k 값 변하지 않도록 tmp로 설정할 것
+6
'''
from itertools import permutations
def solution(k, dungeons):
    answer = []
    n = len(dungeons)
    for per in permutations(dungeons, n):
        cnt = 0
        tmp = k
        for p in per:
            if tmp >= p[0]:
                tmp -= p[1]
                cnt += 1
            else:
                break
        answer.append(cnt)
    return answer

k, dungeons = 80, [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))

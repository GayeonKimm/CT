from itertools import permutations
def solution(k, dungeons):
    answer = []
    n = len(dungeons)
    print(list(permutations(dungeons, n)))
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
    # print(answer)
    return max(answer)

k, dungeons = 80, [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))

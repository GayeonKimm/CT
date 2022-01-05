# level 2
# 소수찾기 완전 탐색
"""
1. 각 숫자를 떼어주기
2. 분리된 숫자들을 순열 조합
3. join을 통해 하나의 숫자로 만들
4. 소수인지 판별
"""

from itertools import permutations
def solution(numbers):
    nums = [n for n in numbers]

    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    new_nums = [int(("").join(p)) for p in per]
    # 소수 판별
    # for n in new_nums:
    #     if n < 2:
    #         continue
    #     check = True
    #     print(n)
    #     for i in range(2, int(n**0.5) + 1):
    #         if n % i == 0:
    #             check = False
    #             break
    #     if check:
    #         answer.append(n)

    # 다른 방법!
    answer = []
    for n in new_nums:
        if n >= 2:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    break
            else:
                answer.append(n)
    return len(set(answer))

numbers = "011"
# numbers = '17'
print(solution(numbers))
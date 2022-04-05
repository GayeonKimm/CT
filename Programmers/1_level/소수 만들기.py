# 소수 만들기
# 숫자들을 combinations합. 3개로 하라고 설정되어 있고
# 만든 숫자 리스트들을 for문 돌리면서 각 숫자들을 더하고
# 더한 그 값이 소수인지 판별

from itertools import combinations
def solution(nums):
    answer = 0
    temp = list(combinations(nums, 3))
    for i in temp:
        s = sum(i)

        for j in range(2, int(s**0.5)+1):
            if s % j == 0: # 소수 아님
                break      # --> for i in temp: 로 돌아가
        # break가 안되면 소수
        else:
            answer += 1
    return answer

nums = [1,2,7,6,4]
# nums = [1,2,3,4]
print(solution(nums))
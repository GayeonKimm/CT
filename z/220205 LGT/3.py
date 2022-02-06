# 개수 찾기
# dp

def solution(k):
    nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    answer = 0

    for i in range(len(nums)):
        if nums[i] == k:
            answer += 1
        for j in range(len(nums)):
            if nums[i]+nums[j] == k:
                answer += 1
                for w in range(len(nums)):
                    if nums[i] + nums[j] + nums[w] == k:
                        answer += 1
                        for h in range(len(nums)):
                            if nums[i] + nums[j] + nums[w] + nums[h] == k:
                                answer += 1
    return answer

print(solution(5))
print(solution(6))
print(solution(9))
print(solution(2))


# combinations 사용 안함
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))

# combinations 사용
from itertools import combinations
def solution(numbers):
    answer = []
    temp = list(combinations(numbers, 2))

    for i in temp:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()
    return answer

# 이렇게 써도 됨
    # for i in temp:
    #     answer.append(sum(i))
    # return sorted(list(set(answer)))


numbers = [2,1,3,4,1]
print(solution(numbers))
# def solution(N, stages):
#     answer = {}
#     temp = len(stages)
#     for stage in range(1, N+1):
#         if temp != 0:
#             count = stages.count(stage)
#             answer[stage] = count/temp
#             temp -= count
#         else:
#             answer[stage] = 0
#     print("answer = ", answer)
#
#     return sorted(answer, key = lambda x:answer[x], reverse = True)


# 재풀이. +6
def solution(N, stages):
    answer = {}
    for i in range(1, N + 1):
        a = stages.count(i)
        b = 0
        for j in range(len(stages)):
            if i <= stages[j]:
                b += 1
        if a == 0:
            answer[i] = 0
        else:
            answer[i] = a / b

    answer = sorted(answer, key=lambda x: answer[x], reverse=True)
    return answer


N, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))

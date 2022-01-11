def solution(N, stages):
    answer = {}
    temp = len(stages)
    for stage in range(1, N+1):
        if temp != 0:
            count = stages.count(stage)
            answer[stage] = count/temp
            temp -= count
        else:
            answer[stage] = 0
    print("answer = ", answer)

    return sorted(answer, key = lambda x:answer[x], reverse = True)



N, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))

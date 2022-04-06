# level 1

def solution(n, lost, reserve):
    reallost = list(set(lost) - set(reserve))
    realres = list(set(reserve) - set(lost))

    # for r in sorted(realres):
    #     if r-1 in reallost:
    #         reallost.remove(r-1)
    #     elif r+1 in reallost:
    #         reallost.remove(r+1)
    # return n - len(reallost)

    #other method
    answer = 0
    for i in sorted(reallost):
        if i-1 in realres:
            realres.remove(i-1)
        elif i+1 in realres:
            realres.remove(i+1)
        else: # 빌려줄 수 없는 경우
            answer += 1
    return n-answer

n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n, lost, reserve))
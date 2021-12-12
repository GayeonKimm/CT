# level 1

def solution(n, lost, reserve):
    reallost = set(lost) - set(reserve)
    realres = set(reserve) - set(lost)

    for r in sorted(list(realres)):
        if r-1 in reallost:
            reallost.remove(r-1)
        elif r+1 in reallost:
            reallost.remove(r+1)

    return n - len(reallost)

n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n, lost, reserve))

# 1. realres 생성해서 비교
# 2. using reallost.remove(r+1)
# 3. n- len(reallost)
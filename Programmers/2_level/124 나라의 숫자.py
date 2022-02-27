# 이건 몇번을 해도 모르겠음 진짜
# +6

def solution(n):
    temp = [1, 2, 4]
    answer = ''
    while n > 0:
        n -= 1
        answer = str(temp[n % 3]) + answer
        n = n//3
    return answer


print(solution(14))
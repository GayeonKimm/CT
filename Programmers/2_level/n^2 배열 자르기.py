'''
이동하는게 나은지
아니면 for문으로 작성하는게 나을지
=> 다틀렸고
'''
# n*n 시간초과
# left, right+1 11번 12번 런타임오류
# int로 감싸기

def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right)+1):
        a = i//n
        b = i % n
        if a < b:
            a, b = b, a
        answer.append(a+1)
    return answer


n,left,right = 4,7,14
print(solution(n,left, right))
# right ~ left까지의 수를 만들기
# 그 수의 약수의 개수 세기
# 약수 갯수가 짝수이면 그 수는 더하고, 홀수면 그 수는 빼기

def solution(left, right):
    answer = 0
    # for i in range(left, right + 1):
    #     cnt = 0
    #     for j in range(1, i+1):
    #         if i % j == 0:
    #             cnt += 1
    #     if cnt % 2 == 0:
    #         answer += i
    #     else:
    #         answer -= i

    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13,17))
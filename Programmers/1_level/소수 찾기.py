def solution(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

n = 10
print(solution(n))


# 효율성 개쓰레기 코드

# def solution(n):
#     num = set(range(2, n+1))
#     answer = len(num)
#     for i in num:
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 answer -= 1
#                 break
#     return answer
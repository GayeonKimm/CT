# 처음에 이렇게 했는데 4점씩이나 받음
# def solution(x,n):
#     answer = [x]
#     temp = x
#     while n > 1:
#         n -= 1
#         temp += x
#         answer.append(temp)
#     return answer

# 클린하다 클린해
def solution(x,n):
    answer = [i*x+x for i in range(n)]
    return answer

x,n = 2,5
print(solution(x,n))
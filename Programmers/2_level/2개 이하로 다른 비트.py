# 비트 = 2진법이였음을....
# 두 글자가 다르면 1을 같으면 0을 반환하는 비트연산자를 사용하였고
# 다른게 2개 이하면 당장 while 종료해서 y반환

# def fx(x):
#     y = x + 1
#     while True:
#         if bin(x ^ y).count('1') <= 2:
#             break
#         else:
#             y += 1
#     return y
#
# def solution(numbers):
#     answer = [fx(i) for i in numbers]
#     return answer

# 시간초과로 실패

# method 2
def solution(numbers):
    answer = [fx(i) for i in numbers]
    return answer


numbers = [2,7]
print(solution(numbers))
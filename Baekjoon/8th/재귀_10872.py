# 1116
# 10872 팩토리얼
# def factorial(n):
#     result = 1
#     if n > 0:
#         result = n*factorial(n-1)
#     return result
# n = int(input())
# print(factorial(n))

# n이 0이면 0!=1 반환 할 수 있도록 설정
# for문으로 작성해볼까
n = int(input())
result = 1
for i in range(1, n+1):
    result = result * i
print(result)
# 이거는 1 고려 안한거니까 다듬으면

n = int(input())
result = 1
if n >0:
    for i in range(1, n+1):
        result*=i
print(result)
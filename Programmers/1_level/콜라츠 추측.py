# 콜라츠 추측
# 500번 한정짓기가 포인트

# 이거 하나 틀림...

# def solution(num):
#     for i in range(500):
#         num = num/2 if num%2==0 else num*3+1
#         if num == 1:
#             return i+1 # 시행한 횟수 return
#     return -1

# method
def solution(num):
    answer = 0

    while True:
        if num==1:
            return answer
        if answer == 500:
            return -1
        num = num/2 if num%2==0 else num*3+1

        answer += 1

# print(solution(6))
print(solution(626331))
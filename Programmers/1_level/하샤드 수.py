# def solution(x):
#     answer = True
#     a1 = x%10
#     a2 = x//10
#     if x%(a1+a2)==0:
#         return answer
#     else:
#         answer = False
#         return answer
# 일의 자리, 십의자리 하나씩 뽑을건데
# 그러면 백의 자리는 어떡하지,
# 오류남

# method
def solution(x):
    answer = [int(i) for i in str(x)]
    if x%sum(answer)==0:
        return True
    else:
        return False

print(solution(12))
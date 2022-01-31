# def solution(s):
#     answer = []
#     for i in s:
#         if not answer:
#             answer.append(i)
#         else:
#             if answer[-1] != i:
#                 answer.append(i)
#     return answer

# 이렇게 하면 stack 유무 신경 안써도 되긴 함!!!
# 이 코드가 효율성이 약간 더 좋음

def solution(s):
    answer = ['*']
    for i in s:
        if i != answer[-1]:
            answer.append(i)
    return answer[1:]

s = [1,1,2,3,2,4,6,1,0,0,0,0,1,1]
print(solution(s))
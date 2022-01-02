# 숫자 문자열과 영단어

# list

def solution(s):
    answer = s
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for a in alpha:
        if a in answer:
            answer = answer.replace(a, str(alpha.index(a)))
    return int(answer)

# dictionary

# def solution(s):
#     answer = s
#     alpha = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
#     for a in alpha.items():
#         answer = answer.replace(a[0], str(a[1]))
#     return int(answer)


print(solution("one4seveneight"))
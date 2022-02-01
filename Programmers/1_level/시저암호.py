# def solution(s, n):
#     answer = ''
#     for i in range(len(s)):
#         if s[i].isupper():
#             answer += chr((ord(s[i]) - ord('A') +n)%26 + ord('A'))
#         elif s[i].islower():
#             answer += chr((ord(s[i]) - ord('a') +n)%26 + ord('a'))
#         else:
#             answer += ' '
#     return answer
# 처음ㅇ에 한 거는 answer에 그대로 담았고, 공백도 따로 담음

# 근데 이런 방식으로 하니까 그럴 필요가 없드라고요
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n)%26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n)%26 + ord('a'))
    return ''.join(s)

# s,n = "AB", 1
s,n ="a B z", 4
print(solution(s,n))
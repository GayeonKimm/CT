# + 6
'''
글자 확인해서 stack에 담아두기
일단 넣어두고
이 문자가 스택에 방금 넣은 것과 같으면 이 문자도 지우고
'''
def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    if stack:
        return 0
    else:
        return 1

print(solution('baabaa'))
def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    return stack == []

s = "(())()"
s1 = "(()("
print(solution(s))
print(solution(s1))
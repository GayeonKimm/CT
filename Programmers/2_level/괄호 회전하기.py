# 재풀이 +7

def check(temp):
    stack = []
    for i in temp:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if len(stack) == 0:
            # if not stack:
                return False
            x = stack.pop()
            if i == ')' and x != '(':
                return False
            elif i == ']' and x != '[':
                return False
            elif i == '}' and x != "{":
                return False
    return len(stack) == 0
# stack에 아무것도 없으면 True 반환, 아니면 False 반환

def solution(s):
    temp = s
    answer = 0
    for i in range(len(s)):
        temp = temp[1:] + temp[0]
        print(temp)
        if check(temp):
            answer += 1
    return answer

s = "[](){}"
# s = "}]()[{"
# s = "[)(]"
# s = "}}}"
print(solution(s))
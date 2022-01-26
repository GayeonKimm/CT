
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

# deque를 사용한 버전
# 1
# from collections import deque
# def solution(s):
#     temp = deque(s)
#     answer = 0
#
#     for i in range(len(s)):
#         tmp = temp.popleft()
#         temp.append(tmp)
#         if check(temp):
#             answer += 1
#     return answer


# 사용 안한 버전
# 2
def solution(s):
    temp = s
    answer = 0
    for i in range(len(s)):
        temp = temp[1:] + temp[0]
        if check(temp):
            answer += 1

    return answer

s = "[](){}"
# s = "}]()[{"
# s = "[)(]"
# s = "}}}"
print(solution(s))
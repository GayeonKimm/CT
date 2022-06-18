'''
if s[i-1] == '(':  - > 바로 직전 문자면 종료하고 연산 계속하는데
그게 아니니까 원래 문자열에서 봐야함ㅠ
'''

import sys
input = sys.stdin.readline

s = input().strip()

# 올바른 괄호인지 판단
# def check(temp):
#     stack = []
#     for i in temp:
#         if i == '(' or i == '[':
#             stack.append(i)
#         else:
#             if len(stack) == 0:
#                 return False
#
#             x = stack.pop()
#             if i == ')' and x != '(':
#                 return False
#             elif i == ']' and x != '[':
#                 return False

# 계산하는 코드
stack = []
temp = 1
answer = 0

for i in range(len(s)):
    if s[i] == '(':
        temp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        temp *= 3
        stack.append(s[i])

    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if s[i-1] == '(': #
            answer += temp
        stack.pop()
        temp = temp // 2 # 다시 1로 만들어두기

    else:
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if s[i-1] == '[': # 이게 무슨 차이여?
            answer += temp
        stack.pop()
        temp = temp // 3 # 다시 1로 만들어 두기

if stack:  # break가 아니여도 남아있는게 있다면
    answer = 0
# 이거 빼면 틀림~!
print(answer)
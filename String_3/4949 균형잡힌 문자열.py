import sys
input = sys.stdin.readline
'''
문자열이 균형이 잡힌지 확인하는 방법
괄호가 들어오면 마지막 저장된 괄호랑 짝 맞느지 확인
'''

while True:
    A = input().rstrip()     #오른쪽만 공백 제거하고
    stack = []
    if A == '.':
        break

    for i in A:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

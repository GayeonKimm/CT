# 2743 단어 길이 재기
# A = input()
# print(len(A))


# A = input()
# print(A[-1])

# 4949 균형
while True:
    A = input()
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

# 알고리즘은 이해 되는데 전반적인 방식의 이해는 완전히 안됨

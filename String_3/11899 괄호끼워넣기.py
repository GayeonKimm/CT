'''
솔직히 아는 문제지만 해석이 어렵다고 생각해서 복잡하게 해결함
나는 .. 나는

'''
import sys
input = sys.stdin.readline

s = input().strip()
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if stack and stack[-1] =='(':
            stack.pop()
        else:
            stack.append(s[i])
    print(stack)
print(len(stack))

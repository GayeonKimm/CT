'''
올바른 괄호이면 YES
그렇지 않으면 NO 출력
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input()
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print('NO')
                break
            elif stack[-1] == '(':
            # else:
                stack.pop()

    else: # break로 넘어가지 않았을때!!
        print('**')
        if not stack:
            print('YES')
        else:
            print("NO")
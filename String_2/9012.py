import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    # break문으로 끊기지 않고 수행 됐을경우 수행
    else:
        if not stack:  # break문으로 안끊기고 스택이 비어있다면 YES
            print("YES")
        else:           # break안 걸렸더라도 스택에 괄호가 들어있다면 NO
            print("NO")

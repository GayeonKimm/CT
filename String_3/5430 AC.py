'''
틀린 정답임
수정 필
'''

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
while t > 0:
    t -= 1
    func = list(input().strip())
    n = int(input())
    num = list(input().rstrip()[1:-1].split(','))
    q = deque(num)

    check = 0
    if n == 0:
        check = 2 # error

    for i in func:
        if i == 'R':
            if check == 0:
                check = 1
            else:
                check = 0

        elif i == "D":
            if len(q) == 0:
                check = 2 #error
                break
            elif check == 0:
                q.popleft()
            elif check == 1:
                q.pop()

    if check == 0:
        print('[', end='')
        print(','.join(q), end='')
        print(']')

    elif check == 1:
        q.reverse()
        print('[', end='')
        print(','.join(q), end='')
        print(']')

    elif check == 2:
        print("error")

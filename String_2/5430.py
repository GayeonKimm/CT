# AC
# list1 = list(input().rstrip()[1:-1].split(','))
# print(list1)
# print(list1[2])
# sick = list(input().strip())
# print(sick)

# numbers = list(input().rstrip()[1:-1].split(','))
# q = deque(numbers)
# print(q)

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
while T > 0:
    T -= 1
    func = list(input().strip())
    n = int(input())
    numbers = list(input().rstrip()[1:-1].split(','))
    q = deque(numbers)

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

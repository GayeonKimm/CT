import sys
input = sys.stdin.readline

n = int(input())
s = []
answer = []
count = 1

chk = True
for i in range(n):
    num = int(input())

    while count <= num:
        s.append(count)
        answer.append('+')
        count += 1

    if s[-1] == num:
        s.pop()
        answer.append('-')
    else:
        chk = False
if chk:
    for i in answer:
        print(i)
else:
    print('NO')

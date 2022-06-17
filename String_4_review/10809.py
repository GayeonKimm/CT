import sys
input = sys.stdin.readline

s = input().strip()
alpha = 'abcdefghijklmnopqrstuvwxyz'
answer = []
for i in alpha:
    if i in s:
        answer.append(s.find(i))
    else:
        answer.append(-1)

for i in answer:
    print(i, end = ' ')

'''
answer 저장 안하고 바로 print되도록 설정하면 될 듯!
'''

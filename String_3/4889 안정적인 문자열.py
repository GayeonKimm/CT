'''
문자열 열면 닫아야 해
- 괄호 방향을 바꾸는 방법밖에 없음
항상 길이가 짝수다???
도대체 어떻게 푸는 거임?
이 규칙 찾는거 결코 쉬운거 아니라고 생각함
'''

import sys
input = sys.stdin.readline

answer = []
while True:
    s = input().strip()
    cnt = 0
    stack = []
    if '-' in s:
        break

    for i in range(len(s)):
        if not stack and s[i] == '}':
            cnt += 1
            stack.append('{')
        elif stack and s[i] == '}':
            stack.pop()
        else:
            stack.append(s[i])
    cnt += len(stack) // 2 # 이거
    answer.append(cnt)

for i in range(len(answer)):
    print(i+1,'. ', answer[i], sep='')


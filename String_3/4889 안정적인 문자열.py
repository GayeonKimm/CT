'''
문자열 열면 닫아야 해
- 괄호 방향을 바꾸는 방법밖에 없음
}가 들어오면 {로 바꾸자
항상 길이가 짝수다???
'''

import sys
input = sys.stdin.readline

n = 0
while True:
    n += 1
    s = input().strip()
    answer = 0
    if '-' in s:
        break

    for i in range(len(s)):

    print(n,'.', answer)


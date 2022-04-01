# 1316 그룹단어 체커
# find 메소드 사용도 방법

import sys
input = sys.stdin.readline

t = int(input())
answer = t
for _ in range(t):
    s = input().strip()

    # for i in range(len(s)-1):
    #     if s[i] != s[i+1]:
    #         if s[i] in s[i+1:]:
    #             answer -= 1
    #             break

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            pass
        elif s[i] in s[i+1:]:
            answer -= 1
            break
print(answer)
# 1316 그룹단어 체커
# find 메소드 사용도 방법

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    word = input()

    # 마지막은 확인 안해도 됨 len-1
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            N -= 1
            break
print(N)
'''
처음에 헤매다가 해결방법 혼자 완성해나갔다
아이캔두잇
'''

import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
a = list(map(str, input().strip()))
a.reverse()
b = list(map(str, input().strip()))

road = a + b
# print(road)

# 자리 바꾸는 과정
for _ in range(int(input())):
    for i in range(len(road)-1):
        if road[i] in a and road[i+1] in b:
            road[i], road[i+1] = road[i+1], road[i]
            if road[i+1] in a[-1]:
                break

answer = ''
for i in road:
    answer += i
print(answer)
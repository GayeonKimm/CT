# 문자열 폭발

# import sys
# input= sys.stdin.readline
# word = input()
# pop = input()
# for i in range(len(pop)):
#     word = word.replace(pop[i],"")
#
# if len(word)==0:
#     print("FRULA")
# else:
#     print(word)
# 틀렸대

# 스택으로 풀기
import sys
input = sys.stdin.readline

word = list(input().strip())
pop = list(input().strip())

stack = []
for i in range(len(word)):
    stack.append(word[i])
    if stack[-1] == pop[-1] and len(stack) >= len(pop):
        if stack[-len(pop):] == pop:
            for i in range(len(pop)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")


## 더 빠른 방법

import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()
n = len(s)
m = len(p)
lastChar = p[-1]

stack = []
for char in s:
    stack.append(char)
    if char == lastChar and "".join(stack[-m:]) == p:
        del stack[-m:]

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))

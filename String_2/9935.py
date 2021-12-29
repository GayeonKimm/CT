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
# 틀림

# 스택으로 풀기
# word와 pop을 리스트로 받음

# import sys
# input = sys.stdin.readline
#
# word = list(input().strip())
# pop = list(input().strip())
#
# stack = []
# for i in range(len(word)):
#     stack.append(word[i])
#     if stack[-1] == pop[-1] and len(stack) >= len(pop):
#         if stack[-len(pop):] == pop:
#             for i in range(len(pop)):
#                 stack.pop()
#
# if stack:
#     print("".join(stack))
# else:
#     print("FRULA")


# 더 빠르게 내방식대로 재작성
# word와 pop을 string으로 받음

import sys
input = sys.stdin.readline

word = input().strip()
pop = input().strip()
w = len(word)
p = len(pop)
lastChar = pop[-1]

stack = []
for i in word:
    stack.append(i)
    if i == lastChar and "".join(stack[-p:]) == pop: # string으로 받았기 때문에 join 사용
        del stack[-p:]

if stack:
    print("".join(stack))
else:
    print("FRULA")

"""
이거 그냥 기준값
첫글자, 마지막글자만 확인하면 된다 아님?

근데 다른 조건이 있어야 하드라고
1. 주어진 string은 pattern보다 짧아서는 안됨
2. string[:1]은 pattern[0] 이여야 하고 string[-1:]은 pattern[-1]이어야 함!
"""
import sys
input = sys.stdin.readline

n = int(input())
pattern = input().strip().split('*')
# 시작 끝 따로 받아두면 나중에 pattern을 만들었을때와 비교를 못함

for _ in range(n):
    temp = input().strip()

    # temp[:1] == a and temp[-1:] == b 여야 하니까
    if temp[:len(pattern[0])] == pattern[0] and temp[-len(pattern[-1]):] == pattern[-1] and len(''.join(pattern)) <= len(temp):
        print("DA")
    else:
        print("NE")


# 틀린답 - 쉽게 생각한 정답
# a, b = input().split('*')
# for _ in range(n):
#     temp = input().strip()
#
#   # 이거 틀렸다고 함
#   # if temp[0] == pattern[0] and temp[-1] == pattern[-1] and len(''.join(pattern)) <= len(temp):

#     if temp[0] == a and temp[-1] == b:
#         print("DA")
#     else:
#         print("NE")
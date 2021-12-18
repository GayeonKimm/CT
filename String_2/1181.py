# 단어 정렬
import sys
input = sys.stdin.readline

N = int(input())
word = []

for _ in range(N):
    word.append(input().strip())

word = list(set(word))  # set 하고 리스트로 바꿔야됨
word.sort()
word.sort(key=len)

for i in word:
    print(i, end='\n')
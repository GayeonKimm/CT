# 뒤집기
import sys
input = sys.stdin.readline

S = input().strip()
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1
print((count+1)//2)

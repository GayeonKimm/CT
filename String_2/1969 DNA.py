# DNA
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input().strip())

temp = [0 for _ in range(len(s))]

for i in range(len(s)):
    for j in range(len(s[0])):
        temp[i] = s[i][j]


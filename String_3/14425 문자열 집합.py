import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input().strip())
cnt = 0
for _ in range(m):
    a = input().strip()
    if a in s:
        cnt += 1
print(cnt)
#소트인사이드
# 1427
import sys
input = sys.stdin.readline

N = list(map(int, input().strip()))
N.sort(reverse=True)
for i in N:
    print(i, end='')
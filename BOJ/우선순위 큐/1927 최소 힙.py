'''
0이면
- 아무것도 없으면 0
- 있으면 heappop

자연수면 push
'''
import sys
input = sys.stdin.readline

import heapq

min_heap = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else: # 0일 때. 아무것도 없으면
            print(0)
    else:
        heapq.heappush(min_heap, n)

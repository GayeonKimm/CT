'''
최대힙은 두개 넣는 거였어 기억났다

'''
import sys
input = sys.stdin.readline
import heapq

max_heap = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else: # 아무것도 없으면
            print(0)
    else:
        heapq.heappush(max_heap, (-num, num))
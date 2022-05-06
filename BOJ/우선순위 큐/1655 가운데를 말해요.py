import sys
input = sys.stdin.readline
'''
정렬로 풀면 시간초과 오류가 뜸
leftheap, rightheap 사용
'''
import heapq
n = int(input())
left_heap = []
right_heap = []
for _ in range(n):
    num = int(input())
    # input heap
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    # 차례로 외치기
    if right_heap and right_heap[0] < -left_heap[0]: # 더 작은 값
        left = heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right) # 다시 채워넣고
        heapq.heappush(right_heap, -left)
    print(-left_heap[0])
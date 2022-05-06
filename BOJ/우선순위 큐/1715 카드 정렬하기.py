import sys
input = sys.stdin.readline
'''
엥 맞음
변수를 따로 저장하고 
최대한 압축해서 작성해보려고 할 것
'''
import heapq
heap = []
for _ in range(int(input())):
    heapq.heappush(heap, int(input()))

# answer = 0
# while len(heap) > 1:
#     a = heapq.heappop(heap)
#     b = heapq.heappop(heap)
#     heapq.heappush(heap, a+b)
#     answer += (a+b)
# print(answer)

# 예외처리가 있는 다른 사람 코드
answer = 0
if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        plus = heapq.heappop(heap) + heapq.heappop(heap)
        answer += plus
        heapq.heappush(heap, plus)
    print(answer)
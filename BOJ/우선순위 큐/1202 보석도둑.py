import sys
input = sys.stdin.readline
'''
n = 정보, k = 가방 갯수 
1. 주어진 무게 검증
애초에 무게가 안되면 넣을 수 조차 없음

어케 알아내지
2. 주어진 가방 검증
- 여러개 담아야 비교 가능할 거 같은데
-> 비슷한 거 있으면 대기 리스트에 담아두기?
- 다른곳에 담아두는 것도 힘든데?

최대힙을 사용하는 이유 pop쓰려구
'''

import heapq
n, k = map(int, input().strip().split())
# 별 차이 없드라
# j_list = []
# for _ in range(n):
#     heapq.heappush(j_list, list(map(int, input().split())))

j_list = [list(map(int, input().strip().split())) for _ in range(n)]
b_list = [int(input()) for _ in range(k)]
j_list.sort()
b_list.sort()

heap = []
answer = 0
for i in b_list:
    while j_list and i >= j_list[0][0]:
        heapq.heappush(heap, -heapq.heappop(j_list)[1])
        # heapq.heappop(j_list)
    if heap:
        answer += heapq.heappop(heap)
    elif not j_list:
        break
print(-answer)

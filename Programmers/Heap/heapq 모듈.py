import heapq

# 최소 힙 생성, push
heap_list = []
heapq.heappush(heap_list, 4)
heapq.heappush(heap_list, 1)
heapq.heappush(heap_list, 7)
print(heap_list)

# pop
print(heapq.heappop(heap_list))

# pop 하지 않고 최솟값 얻기
print(heap_list[0])

# 기존 리스트를 힙으로 변환
a_list = [4,1,7,3,8,5]
heapq.heapify(a_list)
print(a_list)

# 살짝 변형해보기
b_list = [4,1,7,2,8,5]
b_list.sort()
print("\n변형 전 b_list = ", b_list)
food1 = heapq.heappop(b_list)
food2 = heapq.heappop(b_list)
print("food1 = ", food1)
print("food2 = ", food2)
print("b_list = ", b_list)
heapq.heappush(b_list, food1+food2)
print("push한 b_list = ", b_list)

# 힙에서 인덱스 0이 최솟값이라고 해서, 인덱스 1이 두번째, 2에 세번째 값이 있는 것은 아님
# 두번째로 작은 원소를 얻으려면 heappop()을 이용해 최솟값을 삭제하고,
# heap[0]으로 접근하거나
# 인덱스 1을 인덱스 2와 비교하는 방법을 사용해야 한다.


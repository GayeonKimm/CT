import sys
input = sys.stdin.readline
'''
input : a번 문제는 b보다 먼저 푸는 것이 좋다
위상정렬 + 우선순위 큐 사용
6 5
2 5
3 5
4 1
5 1
4 6
'''
import heapq
n, m = map(int, input().split())
problem = [[] for _ in range(n+1)]
indgree = [0 for _ in range(n+1)]
heap = []
answer = []

# 그래프 정보
for _ in range(m):
    a, b = map(int, input().split())
    problem[a].append(b)
    indgree[b] += 1
print(problem)
print(indgree)

# first heap 만들기
# 먼저 선행되지 않아도 바로 불릴수 있는 것들 먼저 넣기
for i in range(1, n+1):
    if indgree[i] == 0:
        heapq.heappush(heap, i) # 힙에 넣기 때문에 조건3.만족

# make 위상 정렬 loop
while heap:
    temp = heapq.heappop(heap)
    answer.append(temp)
    # 선행되어야 하는 것들 내보내기
    for j in problem[temp]:
        indgree[j] -= 1
        if indgree[j] == 0:
            heapq.heappush(heap, j) # 나갈거 있으면 맨뒤에 push

print(answer)
# for i in answer:
#     print(i, end = ' ')
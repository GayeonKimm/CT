import heapq
def solution(scoville,K):
    answer = 0
    scoville.sort()

    while scoville[0] < K:
        food1 = heapq.heappop(scoville)

        if scoville:
            food2 = heapq.heappop(scoville)
        else:
            return -1

        heapq.heappush(scoville, food1+food2*2)
        answer += 1
        print(scoville)

    return answer

scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville, K))

# push 때는 알아서 sort 되는듯

# 1. About heapq!!
# 2. sort()
# 3. heapq.heappop() / heapq.heappush(scovile, food1 ~ )
# 다익스트라 알고리즘

import heapq
def dijkstra(dis, adj):
    heap = []
    heapq.heappush(heap, [0,1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in adj[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost+c, n])

def solution(N, road, K):
    INF = float('inf')
    dis = [INF] *(N+1)
    # 거리 확인 배열
    dis[1] = 0 # 1번은 자기 자신이니까 거리 0

    adj = [[] for _ in range(N+1)]
    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])

    dijkstra(dis, adj)
    print(dis)
    return len([i for i in dis if i <= K])

# N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4
print(solution(N, road, K))
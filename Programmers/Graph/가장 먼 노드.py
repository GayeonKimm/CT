# method 1
# from collections import deque, Counter
#
# def solution(n, edge):
#     answer = 0
#     graph = {}
#     for i in edge:
#         if i[0] in graph:
#             graph[i[0]].append(i[1])
#         else:
#             graph[i[0]] = [i[1]]
#
#         if i[1] in graph:
#             graph[i[1]].append(i[0])
#         else:
#             graph[i[1]] = [i[0]]
#
#     print("최종 graph = ", graph)
#
#     result = bfs(graph, 1)
#
#     result = sorted(result.values(), reverse=True)
#     return list(Counter(result).values())[0]
#
#
# def bfs(edge, root):
#     visited = {}
#     q = deque([[root, 0]])  # 1과 1은 거리가 0
#     arr = [[root, 0]]  #
#     print("시작 q = ", q)
#
#     while q:   # 비어 있지 않으면 실행
#         current = q.popleft()  # 가장 먼저들어온 거 FIFO 순서
#         print("current = ",current)
#
#         if current[0] not in visited:
#             visited[current[0]] = current[1]
#             add = set(edge[current[0]]) - set(visited)
#             q += ([[i, current[1] + 1] for i in add])
#         print("뭐야? = ",set(edge[current[0]]))
#         print("visited = ", visited)
#         print("add = ", add)
#         print("변하는 q = ", q)
#
#     return visited

from collections import deque

def solution(n, edge):
    answer = 0

    nodes = [[] for _ in range(n+1)]
    for e in edge:
        nodes[e[0]].append(e[1])
        nodes[e[1]].append(e[0])

    dist_list= []

    q = deque([(1,0)])
    visited = [False for _ in range(n+1)]
    visited[1] = True

    while q:
        idx, dist = q.popleft()

        for node in nodes[idx]:
            if not visited[node]:
                visited[node] = True
                q.append((node, dist+1))
                dist_list.append(dist+1)

    answer = dist_list.count(max(dist_list))

    return answer




n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
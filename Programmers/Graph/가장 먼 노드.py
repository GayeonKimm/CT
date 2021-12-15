# method 1

# def solution(n, edge):
#     graph = [set() for _ in range(n + 1)]
#     for s, e in edge:
#         graph[s].add(e)
#         graph[e].add(s)
#
#     queue = set([1])
#     visited = set([1])
#
#     while len(visited) < n:
#         next_queue = set()
#
#         while queue:
#             node = queue.pop()
#             next_queue |= graph[node]
#
#         queue = next_queue - visited
#         visited |= queue
#
#     return len(queue)

from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] * n for _ in range(n + 1)]  # 각 노트와 연결된 노드표시
    print(graph)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    print("graph = ", graph)

    visited = [0] * (n + 1)
    visited[1] = 1
    print("visited = ", visited)
    queue = deque([1])
    print("queue = ", queue)

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[n] + 1
        print(visited)

    answer = visited.count(max(visited))
    return answer



n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
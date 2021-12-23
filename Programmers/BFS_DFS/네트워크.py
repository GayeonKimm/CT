# 네트워크
# level 3


# def solution(n, computers):
#     parent = [x for x in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 pass
#             if computers[i][j]:
#                 for k in range(n):
#                     if parent[k] == parent[i]:
#                         parent[k] = parent[j]
#
#     return len(set(parent))

# dfs
def solution(n, computers):
    def DFS(i):
        visited[i] = True

        for a in range(n):
            if computers[i][a] and not visited[a]: # 처음 들리는 곳이면
                DFS(a)

    answer = 0
    # visited = [0 for i in range(len(computers))]
    visited = [False]*n
    for i in range(n):
        if not visited[i]:  # 방문하지 않았다면
            DFS(i)
            answer += 1
    return answer

# 배웠던 대로 visited 를 bool 자료형으로 만들고


# bfs
# from collections import deque
#
# def solution(n, computers):
#
#     def BFS(i):
#         q = deque()
#         q.append(i)
#         while q:
#             i = q.popleft()
#             visited[i] = 1
#             for a in range(n):
#                 if computers[i][a] and not visited[a]:
#                     q.append(a)
#
#     answer = 0
#     visited =[0 for i in range(len(computers))]
#     for i in range(n):
#         if not visited[i]:
#             BFS(i)
#             answer += 1
#
#     return answer






n= 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers =	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
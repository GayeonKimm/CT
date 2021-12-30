# def solution(citations):
#     answer = []
#     citations.sort()
#     n = len(citations)
#     for i in range(n):
#         up = 0
#         down = 0
#         for j in citations:
#             if i < j:
#                 up += 1
#                 if i == j:
#                     down += 1
#             elif i > j:
#                 down += 1
#
#             if i==up==down:
#                 answer.append(i)
#         print("up =",up, "down = ",down)
#     return answer


def solution(citations):
    citations.sort()
    n = len(citations)
    for h in range(n):
        if citations[h] >= n-h:
            return n-h
    return 0



citations = [3, 0, 6, 1, 5]
print(solution(citations))
# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1,len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer

# 큐를 사용해서
# first in first out
# from collections import deque
# def solution(prices):
#     q = deque(prices)
#     answer = []
#     while q:
#         t = q.popleft()
#         cnt = 0
#         for i in q:
#             cnt += 1
#             if t > i:
#                 break
#         answer.append(cnt)
#     return answer

# 효율성이 더 좋아요
# stack을 이용해서
# last in first out
def solution(prices):
    p = len(prices)
    answer = [i for i in range(p-1, -1, -1)]
    print(answer)

    stack = [0]
    for i in range(1, p):
        print(i, stack)
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
            print(i, j, stack)
        stack.append(i)
    return answer

print(solution([1,2,3,2,3]))
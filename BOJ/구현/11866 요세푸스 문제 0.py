import sys
input = sys.stdin.readline
from collections import deque

def solution(n,k):
    temp = [i for i in range(1, n+1)]
    answer = []
    q = deque(temp)
    while q:
        for i in range(k-1):
            q.append(q.popleft())
        answer.append(q.popleft())
    return answer

n, k = map(int, input().split())
print(solution(n,k))
# print('<' +str(answer)[1:-1]+'>' )
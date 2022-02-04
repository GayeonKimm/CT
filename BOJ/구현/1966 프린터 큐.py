# 수정하고 싶은데 아직 해결 못하는 중 ...!

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, idx = map(int, input().split())
    q = deque(map(int, input().split()))
    idxq = deque(range(0, n))

    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            if idxq.popleft() == idx:
                print(cnt)
                break
        else:
            q.append(q.popleft())
            idxq.append(idxq.popleft())
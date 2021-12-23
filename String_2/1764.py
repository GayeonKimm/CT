# 1764 듣보잡

import sys
input = sys.stdin.readline

N_list = set()
M_list = set()
N, M = map(int, input().split())
for _ in range(N):
    N_list.add(input().strip())
for _ in range(M):
    M_list.add(input().strip())

answer = sorted(list(N_list&M_list))

print(len(answer))
print("\n".join(answer))
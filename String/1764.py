# 1764 듣보잡
N, M = map(int, input().split())
N_list = set()
M_list = set()
for _ in range(N):
    N_list.add(input())
for _ in range(M):
    M_list.add(input())
# print(N_list)
K = list(N_list&M_list)
print(K)
A = sorted(list(N_list&M_list))
print(A)
print(len(A))
for i in A:
    print(i)
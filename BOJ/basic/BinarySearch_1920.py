# 이진 탐색
"""
1. 아이디어
- N개의 숫자를 정렬
- M개를 for문 돌면서 이진탐색 수행
- 이진 탐색 안에서 마지막에 데이터 찾으면 1 아니면 0

2. 시간복잡도
- N개 입력값 정렬 = O(NlgN)
- M개 중에 탐색 = O(M* lgN)
- 총합 : O((N+M)lgN) 가능

3. 자료구조
- N개 숫자 int[]
- M개 숫자 int[]
"""

# import sys
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))
# result = []
# for i in B:
#     if i in A:
#         result.append(1)
#     else:
#         result.append(0)
# for i in result:
#     print(i)


import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort()   # 정렬 그래야 이진 탐색이 가능함.

def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return

    mid = (st + en)//2
    if nums[mid] < target:
        search(mid+1, en, target)
    else:
        search(st, mid, target)

# 이진 탐색 수행
# 인덱스니까 N-1
for each_target in target_list:
    search(0, N-1, each_target)


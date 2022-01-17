import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
temp = []

for i in range(len(A)):
    if A[0] in B:
        temp += B.index(A[0])


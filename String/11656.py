# 11656 접미사
A = input()
B = []
for i in range(len(A)):
    B.append(A[i:])

# B = sorted(B)
# for i in B:
#     print(i)

# other code
for i in sorted(B):
    print(i)
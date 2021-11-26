# A = [1,2,3,4,5,6]
# B = [2,3,4,5,6,7,8,9,10]
# A = set(A)
# B = set(B)
# K = list(A&B)
# print(K)

# 1100 하얀 칸
# 변수 설정을 다시 했음 (sum -> answer)
A = []
for _ in range(8):
    A.append(list(map(str, list(input()))))
answer = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if A[i][j] == 'F':
                answer += 1
print(answer)
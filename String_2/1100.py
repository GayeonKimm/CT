# A = [1,2,3,4,5,6]
# B = [2,3,4,5,6,7,8,9,10]
# A = set(A)
# B = set(B)
# K = list(A&B)
# print(K)

# 1100 하얀 칸
C =[]
for _ in range(8):
    C.append(list(map(str,list(input()))))

sum = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if C[i][j] == 'F':
                sum +=1
print(sum)
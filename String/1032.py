# a =['h','e','y']
# print('+'.join(a))
# # result =[]
# result =''
# for i in a:
#     result += i
# print(result)



# 1032
n = int(input())
A = list(input())
for i in range(n-1):
    B = list(input())
    for j in range(len(A)):
        if A[j] != B[j]:
            A[j] ='?'
print(''.join(A))
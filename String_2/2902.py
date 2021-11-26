# 2902
A = list(input().split('-'))
ans = ''
for i in range(len(A)):
    ans += A[i][0]
print(''.join(ans))
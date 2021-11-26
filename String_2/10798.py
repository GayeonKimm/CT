# 10798 세로 읽기

# A = []
# for _ in range(5):
#     A.append(list(input()))
# ans = ''
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         ans += A[j][i]
# print(''.join(ans))

# ERROR CODE 런타임에러

# A = []
# for _ in range(5):
#     A.append(list(input()))
#
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[j][i], end ='')

A = []
for _ in range(5):
    A.append(list(input()))
# A에서 제일 긴 문장 기준

for i in range(max([len(e) for e in A])):
    for j in range(5):
        if i < len(A[j]):
            print(A[j][i], end ='')

# 제일 긴 문장 기준에 비해 문자열이 없으면 넘어가는 if문 추가
# 문장으 5개 입력 받았으므로 range(5) 고정
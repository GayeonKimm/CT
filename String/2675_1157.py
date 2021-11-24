#2675
# n = int(input())
# for i in range(n):
#     t, case = input().split()
#     for j in range(len(case)):
#         print(case[j]*int(t), end ='')
#     print()

# 1157
A = input().upper()
A_list = list(set(A))
cnt =[]
for i in A_list:
    count = A.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(A_list[cnt.index(max(cnt))])
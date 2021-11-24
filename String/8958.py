
# 8958
# n = int(input())
# sum = 0
# k = 1
# for i in range(n):
#     c = input()
#     for j in c:
#         if j =='O':
#             sum += k
#             k += 1
#         else:
#             k = 1
#     print(sum)

n = int(input())
for i in range(n):
    c = input()
    sum = 0
    k = 1
    for j in c:
        if j =='O':
            sum += k
            k += 1
        else:
            k = 1
    print(sum)

# c와 sum 을 넣는 위치의 중요성
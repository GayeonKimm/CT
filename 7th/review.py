# 달팽이
# a, b, v = map(int,input().split())
# if (v-b)%(a-b)==0:
#     n = (v-b)//(a-b)
# else:
#     n=(v-b)//(a-b)+1
# print(n)
# 왜 if가 0일때인지 이유가 뭐야?

# 호텔
# t = int(input())
# for i in range(t):
#     h,w,n = map(int,input().split())
#     if n % h == 0:
#         n_th = h
#         n_r = n//h
#     else:
#         n_th = n % h
#         n_r = n//h + 1
#     print(n_th*100+n_r)

# 부녀회장
# t = int(input())
# for _ in range(t):
#     k = int(input())
#     n = int(input())
#     people = [i for i in range(1, n+1)]
#
#     for _ in range(k):
#         for y in range(1,n):
#             people[y] += people[y-1]
#     print(people[-1])
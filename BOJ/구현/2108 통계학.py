import sys
input = sys.stdin.readline

N = int(input())
a = [int(input()) for _ in range(N)]
a.sort()

# 산술평균
print(round(sum(a)/N))

# 중앙값
print(a[N//2])

# 최빈값
# x = {}
# for i in a:
#     if i in x:
#         x[i] += 1
#     else:
#         x[i] = 1
# x = sorted(x.items(), key=lambda x:x[1], reverse=True)
#
# if N != 1:
#     if x[0][1] == x[1][1]:
#         print(x[1][0])
#     else:
#         print(x[0][0])
# else:
#     print(x[0][0])

from collections import Counter
a_s = Counter(a).most_common()
if len(a_s) > 1:
    if a_s[0][1] == a_s[1][1]:
        print(a_s[1][0])
    else:
        print(a_s[0][0])
else:
    print(a_s[0][0])

# 범위
print(int(a[-1] - a[0]))
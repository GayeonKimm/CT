# 15596 정수 N개의 합
# def solve(a):
#     return sum(a)
#
# def solve1(a):
#     total = 0
#     for i in a:
#         total += i
#     return total
#
#
# print(solve([1,2,3,4,5]))
# print(solve1([1,2,3,4,5]))

# 4673 셀프 넘버
# 자리수 뽑지 말고 문자 취급한다음에 다시 숫자로 생각하면 됨
def d(n):
    m = n
    for i in str(n):
        m+=int(i)
    return m

list_d =[]
for i in range(10000):
    list_d.append(d(i))

list_a = []
for i in range(10000):
    list_a.append(i)

# set으로 해도 되고 list끼리 비교해서 봐도 됨
self_numbers = list(set(list_a)-set(list_d))
print(self_numbers)

self_numbers = sorted(self_numbers)
for i in self_numbers:
    print(i)
def maketable(p):
    kmptable = [0 for _ in range(len(p))]

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = kmptable[j-1]

        if p[i] == p[j]:
            j += 1
            kmptable[i] = j

    return kmptable

def kmp(t, p):
    table = maketable(p)
    # print(table)

    count = 0
    result = []

    j = 0
    for i in range(len(t)):

        while j > 0 and t[i] != p[j]:
            j = table[j - 1]

        if t[i] == p[j]:
            if j == (len(p) - 1):
                result.append(i - len(p) + 2)
                count += 1
                j = table[j]
            else:
                j += 1

    print(count)
    print(*result)
    # for i in result:
    #     print(i)
    # return count, result

# import sys
# input = sys.stdin.readline
# 이거쓰고 틀려버림...!!!!!!!!!!!!!!!

t = input()
p = input()
kmp(t, p)

# count, result = kmp(t, p)
# print(count)
# for i in result:
#         print(i)

# print(*result)

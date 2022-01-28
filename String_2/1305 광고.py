def maketable(p):
    table = [0 for _ in range(l)]

    j = 0
    for i in range(1, l):
        print("i, j = ", i, j)
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

l = int(input())
ptn = input()
print(maketable(ptn))
# print(l-maketable(ptn)[l-1])
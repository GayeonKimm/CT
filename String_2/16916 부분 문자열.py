def maketable():
    table = [0 for _ in range(len(p))]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def kmp(s,p):
    table = maketable()

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == len(p)-1:
                return True
            else:
                j += 1
    return False

s = input()
p = input()
if kmp(s,p):
    print(1)
else:
    print(0)
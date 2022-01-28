# 문자 하나에서 확인하면 되니깐은
def maketable(p):
    table = [0 for _ in range(len(p))]

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    # print(table)
    return max(table)

s = input()
answer = 0
for i in range(len(s)):
    sub = s[i:len(s)]
    # print(sub)
    answer = max(answer, maketable(sub))
print(answer)
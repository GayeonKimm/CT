import sys
input = sys.stdin.readline

t = input().strip()
p = input().strip()

kmptable = [0 for _ in range(len(p))]
def maketable(p,kmptable):
    j = 0
    for i in range(1, len(p)):
        while j>0 and p[i] != p[j]:
            j = kmptable[j-1]
        if p[i]==p[j]:
            j+=1
            kmptable[i] = j
def kmp(t,p,kmptable):
    maketable(p,kmptable)
    j = 0
    count = 0
    result = []
    p_size = len(p)
    for i in range(len(t)):
        while j > 0 and t[i]!=p[j]:
            j=kmptable[j-1]
        if t[i]==p[j]:
            if j==p_size-1:
                count += 1
                result.append(i-p_size+2)
                j = kmptable[j]
            else:
                j+=1
    return count, result
import sys
input = sys.stdin.readline

s = list(input().strip())
answer = []
for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        a = s[:i]
        b = s[i:j]
        c = s[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        temp = a+b+c
        answer.append("".join(temp))
print(sorted(answer)[0])


# brus 방법
# s = input()
# li = []
# for i in range(len(s)-2):
#     for j in range(i+1, len(s)-1):
#         for k in range(j+1, len(s)):
#             t = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
#             li.append(t)
# print(min(li))
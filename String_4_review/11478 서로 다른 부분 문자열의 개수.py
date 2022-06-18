import sys
input = sys.stdin.readline

s = input().strip()
answer = []
temp = ''
for i in range(len(s)):
    for j in range(len(s)-i):
        temp += s[j:j+i+1]
        answer.append(temp)
        temp = ''
# print(answer)
# print(len(answer))
print(len(list(set(answer))))

# 다른 방법!!!!!!!!
ans = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        tmp = s[i:j+1]
        ans.add(tmp)
print(len(ans))

import sys
input = sys.stdin.readline

# 방법 1
from collections import Counter

answer = []
while True:
    n = input().strip()
    if not n:
        break
    answer.append(n)
c = Counter(answer)
ans = sorted(list(set(answer)))
for i in ans:
    # prop = c[i]/len(answer)*100
    # print(i, round(prop, 4))
    print(f'{i} {((c[i] / len(answer)) * 100):.4f}')


# 방법 2 - dictionary 사용
d = {} # full ver
d_names = [] # 이름 담아놓을 용도
cnt = 0

while True:
    name = input().strip()
    if not name:
        break
    cnt += 1
    if name not in d:
        d[name] = 1
        d_names.append(name)
    else:
        d[name] += 1

d_names.sort()
for i in d_names:
    print(f'{i} {((d[i]/cnt)*100):.4f}') # 이거 이렇게 해야 맞음
    # print(i, round(d[i]/cnt*100,4)) # 틀림

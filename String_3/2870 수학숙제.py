'''
한 문장 들어올 때 숫자이면 temp에 이어 붙이고
answer에 숫자로 어펜드
정렬 후 하나씩 출력
맘에 안든다...
'''
import sys
input = sys.stdin.readline

answer = []
# 정규 표현식으로 문제 풀기 - 시간은 더 오래걸리긴 함
# import re
# for _ in range(int(input())):
#     s = input().strip()
#
#     p = re.compile('[0-9]+') # 숫자인 것들 검색어
#     m = p.findall(s) # s에서 찾아봐
#     for i in m:
#         answer.append(int(i))
# answer.sort()
# for i in answer:
#     print(i)

# 그냥 생각나는대로 푼

for _ in range(int(input())):
    temp = ''
    s = input().strip()
    for i in s:
        if i.isnumeric():
            temp += i
        else:
            if temp:
                answer.append(int(temp))
                temp = ''
    if temp:
        answer.append(int(temp))
answer.sort()
for i in answer:
    print(i)

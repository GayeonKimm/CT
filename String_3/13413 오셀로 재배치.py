'''
2개 서로 자리를 바꾸기
--> 자리를 바꾼다는건 색을 바꾼다는 것 아닐까?
하나 바꾸기
만약 다른 것이 초기에 WWB이면 W와B는 서로 위치만 바꿔주면 되는 문제
즉 비슷한 상황을 나열해보면 더 큰 숫자가 정답이됨
'''

import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    temp = []
    n = int(input())
    fir = input().strip()
    end = input().strip()
    for i in range(n):
        if fir[i] != end[i]:
            temp.append(fir[i])

    if temp.count('W') >= temp.count('B'):
        answer.append(temp.count('W'))
    else:
        answer.append(temp.count('B'))

for i in answer:
    print(i)
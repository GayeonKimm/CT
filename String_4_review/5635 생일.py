'''
정렬문제 같은디용
'''

import sys
input = sys.stdin.readline

answer = []
for i in range(int(input())):
    name, day, month, year = input().strip().split()
    answer.append([name, int(year), int(month), int(day)])
answer.sort(key=lambda x:(x[1],x[2], x[3])) # 생일 빠른순 정렬
print(answer[-1][0])
print(answer[0][0])
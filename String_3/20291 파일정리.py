import sys
input = sys.stdin.readline
'''
** 딕셔너리 정렬하는 문제 **
어떻게 하는게 조을까
.이 나오면 나눠서 저장해두는겨
거기에 +1 씩
'''

a = {}
n = int(input())

for i in range(n):
    name, f = input().strip().split('.')
    if f not in a:
        a[f] = 1
    else:
        a[f] += 1

answer = sorted(a.items()) # 딕셔너리 정렬하기!!!!!!!!!!!!!!!!

for i, j in answer:
    print(i, j)
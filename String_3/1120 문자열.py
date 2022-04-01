'''
문자 길이의 차이가 존재하면 계속 아무 알파벳이나 추가
1이상 차이가 나면 양쪽에 다 추가할 수 있어서 모든 경우의 수 다 생각
존재하는위치와 문자가 모두 같아야 함
차이가 나면 count 세는거임 같으면 하는게 아니고
a가 더 작은 거고 b가 정답이 되는
아 그니까 추가하라고 했다고 추가하는 문제가 아닌...
'''

import sys
input = sys.stdin.readline

a, b = input().split()
answer = []
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            count += 1
    answer.append(count)

print(min(answer))
'''
영어로 대체 해야겠구만? - 맞긴 하구만
- 리스트말고 딕셔너리로 조합도 하네
- join 사용해서 연결했네
'''

import sys
input = sys.stdin.readline

m,n = map(int, input().split())
nums = [i for i in range(m,n+1)]
n = []
al = ['zero','one', 'two', 'three', 'four', 'five','six', 'seven','eight', 'nine']
for i in range(len(nums)):
    read = []
    num = str(nums[i])
    for j in range(len(num)):
        read.append(al[int(num[j])])
    n.append([read,int(num)])

n.sort(key=lambda x:x[0])
for i in range(len(n)):
    if i%10 == 0 and i != 0:
        print()
    print(n[i][1], end=' ')
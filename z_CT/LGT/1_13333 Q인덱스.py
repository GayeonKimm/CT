import sys
input = sys.stdin.readline

def solution(n,temp):
    for i in range(n, -1, -1):
        if i <= temp[-i]:
            return i

n = int(input())
temp = sorted(list(map(int, input().split())))
print(solution(n,temp))
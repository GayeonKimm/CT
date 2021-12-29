# 5052 전화번호 목록

import sys
input = sys.stdin.readline
t = int(input())

def check():
    for i in range(len(ph)-1):
        if ph[i] == ph[i+1][:len(ph[i])]:
            print("NO")
            return
    print("YES")

for _ in range(t):
    n = int(input())
    # ph = []
    # for i in range(n):
    #     ph.append(input().strip())
    ph = [input().strip() for _ in range(n)]
    ph.sort()  # 정렬사용해서 앞뒤 문자만 확인하기
    check()

k = int(input())
def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n%2 == 0:
        return solution(n//2)
    else:
        return 1 - solution(n//2)

# 인덱스 접근이 아니라 몇번째인지 물어보는 문제라서 k-1 했음

print(solution(k-1))
'''
+6

규칙 잘찾음
1,2, 3,4, 5,6, 7,8 일때
1,    2,   3,   4 가 되는 규칙
짝수는 //2 이고 홀수는 //2+1 임

두 수가 결국 같아질때까지 경기 진행 +1
'''
def solution(n,a,b):
    answer = 0
    while a != b:
        a = a//2 + a%2 # 짝수면 0이고 홀수면 1이니께
        b = b//2 + b%2
        answer += 1
    return answer

n,a,b = 8,4,7
print(solution(n,a,b))
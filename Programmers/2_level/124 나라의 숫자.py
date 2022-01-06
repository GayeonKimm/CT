#  3이상부터는 십의 자리 수가 생기니까 n = n//3 몫이 없으니께
# 기존에 일의자리 수는 유지하고 새로운 숫자만 추가
# 어렵지만 많이 응용해보자

def solution(n):
    answer = ''
    temp = [1,2,4]

    while n>0: # n이 음수나 0이되면 끝
        n -= 1
        answer = str(temp[n%3]) + answer
        n = n//3
    return answer

print(solution(8))
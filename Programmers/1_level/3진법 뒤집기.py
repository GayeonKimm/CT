def solution(n):
    answer = 0
    result = ''

    while n > 0:
        n,b = divmod(n, 3)
        # print(n,b)
        result += str(b)
    answer = int(result, 3)
    return answer

# divmod : 몫과 나머지 반환

print(solution(45))
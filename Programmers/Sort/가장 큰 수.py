# level2
# 가장 큰 수

def solution(numbers):
    numbers.sort(key = lambda x: str(x)*3, reverse=True)
    # str(x)*3
    if numbers[0] == 0:
        return '0'
    else:
        return "".join(map(str, numbers))

# 테스트케이스 11번에서 실패됨
# return 0 -> return '0'
# 문자로 출력해야해서 그런가봄!


numbers = [6, 10, 2]
print(solution(numbers))





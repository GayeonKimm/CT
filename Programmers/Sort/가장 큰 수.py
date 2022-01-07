# level2

def solution(numbers):
    # numbers.sort(key = lambda x: str(x)*3, reverse=True)
    # sort, sorted 다 가능
    num = sorted(numbers, key= lambda x:str(x)*3, reverse=True)
    if num[0] == 0:
        return '0'
    else:
        return "".join(map(str, num))

    # join 생각 안날때는

    # for i in num:
    #     answer += str(i)
    # return answer


# return 0 -> return '0'
# 문자로 출력해야해서 오류남요
numbers = [6, 10, 2]
print(solution(numbers))





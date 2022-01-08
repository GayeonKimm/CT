# def solution(n):
#     answer = []
#     n = str(n)
#     for i in n:
#         answer.append(int(i))
#     return answer

def solution(n):
    # nu = list(str(n))
    # print(nu)
    # num = map(int, nu)
    # print(num)
    # num_list = list(num)
    # print(num_list)
    num_list = list(map(int, list(str(n))))
    print("num_list = ", num_list)
    sum = 0
    for i in num_list:
        sum += i

    return sum


n = 123
print(solution(n))

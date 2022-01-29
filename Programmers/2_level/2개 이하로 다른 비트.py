# 비트 = 2진법이였음을....
# 두 글자가 다르면 1을 같으면 0을 반환하는 비트연산자를 사용하였고
# 다른게 2개 이하면 당장 while 종료해서 y반환

# def fx(x):
#     y = x + 1
#     while True:
#         if bin(x ^ y).count('1') <= 2:
#             break
#         else:
#             y += 1
#     return y
#
# def solution(numbers):
#     answer = [fx(i) for i in numbers]
#     return answer
# 시간초과로 실패

# method 2

def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = list('0' + bin(num)[2:]) # num을 이진수로 변경
        idx = ''.join(bin_num).rfind('0') # 0이 있는 위치를 찾음
        bin_num[idx] = '1' # 그 자리를 1로 변경
        # 여기까지가 마지막 0을 1로 바꾼 과정 (짝수에게는 걍 num+1)

        # 만약 홀수면
        if num % 2 == 1:
            bin_num[idx+1] = '0' # 1로 바꾼 그 자리 다음을 0으로 변경
        # 이래야 제일 작은 수를 찾는대

        # 2진수를 10진수로 변경하여 answer에 저장
        answer.append(int(''.join(bin_num), 2))
    return answer

numbers = [2,7]
print(solution(numbers))
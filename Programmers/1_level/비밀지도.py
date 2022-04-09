# 재풀이 방법 +2
# def solution(n, arr1, arr2):
#     ar1 = []
#     for i in arr1:
#         tmp = bin(i)[2:]
#         while len(tmp) < n:
#             tmp = '0' + tmp
#         ar1.append(tmp)
#
#     ar2 = []
#     for i in arr2:
#         tmp = bin(i)[2:]
#         while len(tmp) < n:
#             tmp = '0' + tmp
#         ar2.append(tmp)
#
#     answer = []
#     for i in range(n):
#         temp = ''
#         for j in range(n):
#             if ar1[i][j] == '1' or ar2[i][j] == '1':
#                 temp += '#'
#             else:
#                 temp += ' '
#         answer.append(temp)
#     return answer



# bin 비교하는 코드
def solution(n, arr1, arr2):
    answer = []
    temp = []
    temp_str = ''
    for i in range(n):
        temp.append(str(bin(arr1[i] | arr2[i]))[2:].rjust(n, '0'))
        # n 글자수로 만들건데 비어있으면 앞에 0으로 채워

        # 비교
        for j in range(n):
            if temp[i][j] == '1':
                temp_str += '#'
            else:
                temp_str += ' '
        answer.append(temp_str)
        temp_str = ''

    return answer


n,arr1, arr2 = 5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
print(solution(n,arr1, arr2))
# 재풀이 코드 +5
# 10이상의 숫자를 저장하는데 힘들었다
# 숫자 다음엔 무조건 S,D,T가 나온대서 그 부분에 초기화 하는 코드 넣었음

def solution(dartResult):
    answer = 0
    stack = []
    temp = ''
    for i in dartResult:
        if i.isalpha():
            stack.append(int(temp))
            temp = ''
            if i == 'S':
                stack[-1] = stack[-1] ** 1
            elif i == 'D':
                stack[-1] = stack[-1] ** 2
            elif i == 'T':
                stack[-1] = stack[-1] ** 3

        elif i in ['#', '*']:
            if i == '*':
                if len(stack) == 1:
                    stack[-1] = stack[-1] * 2
                else:
                    stack[-1] = stack[-1] * 2
                    stack[-2] = stack[-2] * 2
            else:
                stack[-1] = stack[-1] * (-1)

        elif i.isnumeric():
            temp += i

    answer = sum(stack)
    return answer


print(solution('1D2S#10S'))

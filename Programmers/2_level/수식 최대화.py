# +3

from itertools import permutations
def operations(num1, num2, s):
    # 문자로 들어오기 때문에 int처리 해야됨
    if s == '+':
        return str(int(num1) + int(num2))
    if s == '-':
        return str(int(num1) - int(num2))
    if s == '*':
        return str(int(num1) * int(num2))
def calculate(exp, sign):
    # 주어진 식의 수식과 숫자를 문자로 array에 저장
    array = []
    temp = ''
    for i in exp:
        if i.isdigit():
            temp += i
        else:
            array.append(temp)
            array.append(i)
            temp = ''
    array.append(temp) # 혹시라도 숫자 마지막에 남아 있는게 있다면

    # 계산을 위해 sign 우선순위에 들어간다면 operation 수행,
    # 그렇지 않다면 stack에 차곡 차곡 쌓아두기
    for i in sign:
        stack = []
        while len(array) != 0:
            temp = array.pop(0)
            # 수식 우선순위에 해당된다면
            # 그 전 숫자와 그 다음 숫자 뽑아서 계산돌릴거야
            if temp == i:
                stack.append(operations(stack.pop(), array.pop(0), i))
            # 그렇지 않으면 얌전히 stack에 저장시켜놔
            else:
                stack.append(temp)
        array = stack
    return abs(int(array[0]))

def solution(expression):
    signs = list(permutations(['+', '-', '*'], 3))
    answer = []
    for sign in signs:
        answer.append(calculate(expression, sign))
    return answer


expression = "100-200*300-500+20"
# expression ="50*6-3*2"
print(solution(expression))
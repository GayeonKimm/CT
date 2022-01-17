# 문제에 주어진대로 코드 짜면 됨

def divide(p):
    open_p = 0
    close_p = 0

    # 열고 닫고 갯수 똑같으면 거기까지 기준으로 나눔
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:]

def check(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    #1
    if len(p)==0:
        return ""
    #2
    u,v = divide(p)
    # 잘 나뉜거 u, 그외 V

    #3 u의 올바른 괄호 문자열 확인
    # True라면
    if check(u):
        return u + solution(v)

    #4 아니라면
    else:
        # 빈문자열 answer

        answer = '('
        answer += solution(v)
        answer += ')'

        # u의 첫번째와 마지막 문자 제거
        for p in u[1:len(u)-1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

    return answer


# p = "(()())()"
# p = ")("
p = "()))((()"
print(solution(p))
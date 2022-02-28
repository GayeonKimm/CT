# +4

# 문제에 주어진대로 코드 짜면 됨
def divide(p):
    op = 0
    cl = 0
    for i in range(len(p)):
        if p[i] == '(':
            op += 1
        else:
            cl += 1
        if op == cl:
            return p[:i+1], p[i+1:]

def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if len(p) == 0:
        return ""

    u,v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer


# p = "(()())()"
# p = ")("
p = "()))((()"
print(solution(p))
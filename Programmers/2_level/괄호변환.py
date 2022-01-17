# 문제에 주어진대로 코드 짜면 됨

def divide(p):
    open_p = 0
    close_p = 0
    for i in range(len(p)):
        if p[i]=='(':
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

    #3
    if check(u):
        return u + solution(v)
    #4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for p in u[1:len(u)-1]:
            if p=='(':
                answer+=')'
            else:
                answer += '('
        return answer


p = "(()())()"
# p = ")("
# p = "()))((()"
print(solution(p))
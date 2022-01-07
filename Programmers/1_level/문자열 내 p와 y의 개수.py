# 나중에 짠 코드고
#처음에는 for문 돌면서 p있으면 1 y있음녀 -1해서 리턴했음

def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

print(solution("pPoooyY"))
# 재풀이
# 깝치지 말고 기본에 충실하게....

def solution(s):
    answer = []
    s = s.split(' ')
    print(s)

    for i in range(len(s)):
        temp = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                temp += s[i][j].upper()
            else:
                temp += s[i][j].lower()
        answer.append(temp)

    return ' '.join(answer)

print(solution("try hello world"))
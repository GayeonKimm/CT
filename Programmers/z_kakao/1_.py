'''
성격유형
RT, CF,JM,AN
- 같은 점수면 알파벳 빠른 순

choices 가 4보다 작으면 비동의[0] 그리고 차이가 큰 만큼 점수 부여
4보다 크면 동의[1] 선택이지 차이가 큰 만큼 점수 부여

'''
def solution(survey, choices):
    answer = ''
    maps = [['R','T'], ['C','F'],['J','M'],['A','N']]

    for sur, c in zip(survey, choices):
        cnt = 0
        if c < 4: # 비동의
            cnt += abs(c-4)
        elif c > 4 : # 동의
            cnt += abs(c-4)

    return answer


survey, choices = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
# survey, choices = ["TR", "RT", "TR"], [7, 1, 3]
print(solution(survey, choices))
# 2022년으로 개조했음
# 윤달이면 2월이 28일
# 2022년 1월 1일은 토요일이라서 금요일부터 시작
# 그려보면 알게됨

def solution(a, b):
    answer = b
    month = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED','THU']
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a-1):
        answer += day[i]
    return month[answer % 7]

a,b = 4,30
# a,b = 1,9
print(solution(a,b))
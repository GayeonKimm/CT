import math
def solution(passes, minutes):
    answer = []
    for pas in passes:
        df, dm, pt, pf = pas
        if minutes > dm:
            money = df + math.ceil((minutes - dm)/pt) * pf
        else:
            money = df
        answer.append(money)
    return min(answer)
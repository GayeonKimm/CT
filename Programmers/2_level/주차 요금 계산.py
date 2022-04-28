'''
1. records 분리
2. 시간 분리
- 분으로 계산하는 함수 선언

3. OUT이 안들어오면 자동으로 23:59로 계산
- 이거 어케 확인하지? - 가장 마지막에 들어온 state 확인

4. 차 번호가 빠른 것부터 result 출력
- dictionary에서 그런것도 돼?
-> 안돼... list 로 items 묶고 key로 선언

5. 주차요금 계산
- 올림까지 계산하네.... math ceil 사용 (내림은 floor)
'''

'''
+1점을 받았는데 아마 변수명 복수로 설정을 했거나,
아니면 fees 변수를 따로 선언해두거나!
'''
import math
def datetoM(date):
    h, m = map(int, date.split(':'))
    return h * 60 + m
def solution(fees, records):
    answer = []
    d = {}
    for record in records:
        time, id, state = record.split()
        id = int(id)
        if id in d:
            d[id].append([datetoM(time), state])
        else:
            d[id] = [[datetoM(time), state]]

    temp = list(d.items())
    temp.sort(key=lambda x: x[0])  # 정렬
    # 계산
    for t in temp:
        tt = 0
        for i in t[1]:
            if i[1] == 'IN':
                tt -= i[0]
            else:
                tt += i[0]
        if t[1][-1][-1] == 'IN':
            tt += datetoM('23:59')

        if tt > fees[0]:
            answer.append(fees[1] + math.ceil((tt - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
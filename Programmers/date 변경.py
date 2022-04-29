# datetime 확인
'''
1. 날짜 차이, 날짜가 주어지는 경우
2. 분 차이 , 시간만 주어지는 경우
3. 무슨 요일인지 알아내기 -> list에 담아서 (2016년 문제)
'''
# 1
from datetime import datetime

# 연,월,일
n = datetime.now() # 지금 시간
a = datetime.strptime('20201225', '%Y%m%d')
print((n-a).days) # 일수차이
# print((n-a).minutes) # 분수차이 - 왜 안뜸 ..?
print(int((n-a).seconds/60)) # 분 수차이
print((n-a).seconds) # 초수차이

# 시,분
b = datetime.strptime('18:59', '%H:%M')
c = datetime.strptime('23:59', '%H:%M')
print(int((c-b).seconds/60))


## 2. 분 차이 계산 시, 분으로 들어올 때
records = ["05:34 5961 IN", "06:00 0000 IN",
           "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN",
           "23:00 5961 OUT"]
d = {}
for record in records:
    time, name, state = record.split()
    #### map 반드시 #####
    h,m = map(int, time.split(':'))
    #### 이거 꼭 해줘야함!!!!!!!!!!!!!!! ##########
    total = h*60 + m

    if name in d:
        d[name].append([total, state])
    else:
        d[name] = [[total, state]]
    # if state == 'IN':
    #     if name in d:
    #         d[name] -= total
    # else:
    #     d[name] += total

print(d)


# 3 요일 계산
a, b = 4,30  # 2022년 4월 30일은 무슨 요일이여
daydayday = b
month = [',FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED''THU'] # 2022년 1월 1일이 토요일부터
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(a-1):
    daydayday += day[i]
print (month[daydayday % 7])
"""
0. 마이너 코드들은 하나로 퉁쳐야댐
1. 주어진 시간으로 자르기
- 잘라서 duration으로 저장
-- 자를때 time 조정
--> 분단위로 바꿔서 eduration = end - start
-- 기간만큼 코드 구간 반복

2. code와 m값 비교. 정확히 m이 존재해야만
# 조건
-1 duration이 제일 긴 음악 먼저
-2 먼저 입력된 음악 먼저 --> 걍 먼저 들어온거  뜻이 뭐지...? 시간 시간이 더 작으면 넣는건가

3. answer 값 갱신해가며 최종 title 출력
"""

import math
def solution(m, musicinfos):
    answer = None
    # 코드 변경
    m = m.replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g').replace("A#", 'a')

    for i in range(len(musicinfos)):
        st, ed, title, code = musicinfos[i].split(',')
        # duration 구하기
        # map으로 int변경 해야됨 안하면 str로 남음
        hour, minute = map(int, st.split(':'))
        st = hour*60 + minute # 분단위로 바꿔서

        hour, minute = map(int, ed.split(':'))
        en = hour*60 + minute

        duration = en - st

        # code 마이너 정리
        code = code.replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g').replace("A#", 'a')
        # 기간만큼 반복한 코드 만들기
        code *= math.ceil(duration/len(code))
        code = code[:duration]

        if m not in code:
            continue
        # 비어있으면 일단 넣고 현재 duration이 더 길면 넣고 (duration이 같으면 현재 음악의 시작 시간이 더 작으면(빠르면) 집어 넣음)
        # 먼저 입력된 경우 ... 애매하곤
        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > st):
            answer = (duration, st, title)

    if answer:
        return answer[-1]

    return "(None)"

m,musicinfos = "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
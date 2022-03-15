# 중복 조합
from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_score = 0
    answer = []
    for i in combinations_with_replacement(range(11), n):
        a_score, l_score = 0, 0
        cnt = Counter(i)
        # 카운터 인덱스 접근 가능함

        # info 정보랑 비교하는 과정
        for i in range(11):
            if info[10-i] == 0 and cnt[i] == 0:
                continue
            if info[10-i] >= cnt[i]:
                a_score += i
            else:
                l_score += i

        # 다 돌고 나서
        # 최다 점수차(l_score - a_score) 등록해두는는 과정
        if max_score < (l_score - a_score):
             max_score = (l_score - a_score)
             answer = cnt
             # 정답에도 cnt를 저장해두고

        # 같은 날이 발생하면, 그 중에서 최저 점수가 있는 리스트를 확인하는 과정
        elif max_score == (l_score - a_score) and max_score != 0:
            if answer == []:
                answer = cnt
                # 비어 있다면 그게 정답이지
            # 근데 그게 아닐때
            else:
                for i in range(11):
                    if answer[i] == 0 and cnt[i] == 0:
                        continue
                    if answer[i] < cnt[i]:
                        answer = cnt
                        break
                    elif answer[i] > cnt[i]:
                        break

    if not answer:
        return [-1]
    else:
        temp = answer
        answer = [0]*11
        for i in range(11):
            answer[10-i] = temp[i]
    return answer

n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))
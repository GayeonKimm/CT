# Counter 사용
# 소문자 적용
# 2문자씩 슬라이싱(영어만 허용)
# 두 리스트의 counter적용
# inter:교& / union : 합| ==> 해당 값들은 리스트에 저장되도록
from collections import Counter
def solution(str1, str2):
    s1 = str1.lower()
    s2 = str2.lower()
    s11, s22 = [], []

    for i in range(len(s1)-1):
        if s1[i].isalpha() and s1[i+1].isalpha():
            s11.append(s1[i:i+2])
            # s11.append(s[i]+s[i+1]) # 이것도 됨!
    for i in range(len(s2)-1):
        if s2[i].isalpha() and s2[i+1].isalpha():
            s22.append(s2[i:i+2])

    c1 = Counter(s11)
    c2 = Counter(s22)

    # 부호 조심 &:교, |:합
    inter = list((c1&c2).elements())
    union = list((c1|c2).elements())

    if len(union) == 0:
        return 65536
    else:
        return int(len(inter)/len(union) * 65536)


str1, str2='FRANCE', 'french'
# str1, str2 = 'handshake', "shake hands"
print(solution(str1,str2))
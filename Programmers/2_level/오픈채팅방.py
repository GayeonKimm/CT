# dic에 유저 정보 저장하고
# 다시 record돌려서 leave일때, Enter일때 answer에 추가

def solution(record):
    answer = []
    # 유저 정보 담을 dic
    dic = {}

    for i in record:
        sp = i.split()
        if len(sp) == 3:
            # enter와 change정보만을 반영하기 위해 길이 제한.
            # 어차피 change가 이전값 갱신하기 때문
            dic[sp[1]] = sp[2]

    for i in record:
        temp = i.split()
        if temp[0] == 'Enter':
            answer.append("%s님이 들어왔습니다." %dic[temp[1]])
            # %s 사용법

        elif temp[0] == 'Leave':
            answer.append("%s님이 나갔습니다." %dic[temp[1]])

    return answer



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
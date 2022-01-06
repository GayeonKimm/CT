# {{}} 부분을 제거하고 가야됨!
# 순서에 맞게 넣어야하는데 sort로 길이 순으로 정렬하면 딱 맞음

def solution(s):
    temp = [i.split(',') for i in s[2:-2].split("},{")]
    # s[2:-2]인 것을 "},{"으로 분리한걸 i라고 함
    # 그 i를 다시 ,을 기준으로 나눠서 temp에 넣음
    # [['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']]

    temp = sorted(temp, key=len)
    answer = []
    # 방법이 없음 2차원 배열이니까 이중 for문으로 확인해야돼 주저 말고 시도할 것 =
    for i in temp:
        for j in i:
            # 여기서 int 둘다 안하면 어떤건 문자로 인식해서 계속 집어넣더라
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
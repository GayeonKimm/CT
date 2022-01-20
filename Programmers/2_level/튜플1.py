def solution(s):
    temp = [i.split(',') for i in s[2:-2].split("},{")]

    temp = sorted(temp, key=len) # 개수 순서대로 오름차순
    print(temp)

    answer = []
    for i in temp:
        for j in i:
            # if int 설정하지 않으면 문자로 인식해서 계속 집어넣음
            if int(j) not in answer:
                answer.append(int(j))
    return answer


# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
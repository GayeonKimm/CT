# 헷갈리는게 너무 많아서 익숙해질때까지 확인해볼 것

def solution(s):
    strings = s.split()
    print(strings)
    for i in range(len(strings)):
        s_list = list(strings[i])
        print(s_list)
        for j in range(len(s_list)):
            if j%2 == 0:
                s_list[j] = s_list[j].upper()
            elif i%2 == 1:
                s_list[j] = s_list[j].lower()
        print(s_list)
        strings[i] = ''.join(s_list)
        print(strings)
    answer = ' '.join(strings)
    # 공백 있게 join

    return answer

print(solution("try hello world"))
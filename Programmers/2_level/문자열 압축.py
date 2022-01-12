def solution(s):
    answer = []
    if len(s)==1:
        return 1

    for i in range(1, int(len(s)/2)+1):
        b = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            print("i , j = ",i,j)
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:  # 같으면
                    b = b+str(cnt)+tmp
                else:
                    b = b+tmp
                tmp = s[j:j+i]
                cnt = 1

        if cnt != 1:
            b = b+str(cnt)+tmp
        else:
            b = b+tmp
        answer.append(len(b))
    print(answer)
    return min(answer)



# print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
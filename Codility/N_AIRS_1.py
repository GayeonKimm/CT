def solution(S):
    if len(S) <= 3:
        if S.count('a') <= 2 :
            return 0
        else:
            return 1
    else:
        tmp =[]
        answer =[]

        for i in range(1,len(S)-1):
            for j in range(i+1,len(S)):
                tmp.append(S[:i])
                tmp.append(S[i:j])
                tmp.append(S[j:])
        print(tmp)

    # for a in tmp:
    #     answer.append(''.join(a))

    # return answer

    pass

print(solution('babaa'))  #2
# print(solution('ababa'))  #4
# print(solution('aba'))    #0
# print(solution('bbbbb'))  #6
# print(solution('aaa'))    #1

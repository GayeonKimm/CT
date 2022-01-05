def solution(new_id):
    #1
    new_id = new_id.lower()

    #2
    answer = ''
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    answer = answer[1:] if answer[0]=='.' and len(answer)>1 else answer
    answer = answer[:-1] if answer[-1]=='.' else answer

    if len(answer)==0:
        answer = 'a'
    #6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
    #7
    while len(answer) < 3 :
        answer += answer[-1]
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
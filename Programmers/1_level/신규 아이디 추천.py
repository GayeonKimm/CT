def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    if len(new_id) == 0:
        new_id = 'a'
        makeid(new_id)


def makeid(new_id):
    if 3 <= len(new_id) <= 16:
        for i in range(len(new_id)):
            if new_id[i] in :


    elif len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))
        makeid(new_id)

    elif len(new_id) > 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.remove(new_id[-1])
            makeid(new_id)

    return answer
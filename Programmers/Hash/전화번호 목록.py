def solution(phone_book):
    answer = True
    ph = sorted(phone_book)

    for i in range(len(ph)-1):
        # 길이 비교 해도 정답이고 아니여도 정답이긴함
        # 근데 앞에 있다는건 접두사일수 밖에 없을 듯
        if len(ph[i]) < len(ph[i+1]):
            if ph[i] == ph[i+1][:len(ph[i])]:
                answer = False
                break   #하나만 있어도 False니까 break

    return answer


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
# 재풀이 +5

def solution(phone_book):
    answer = True
    ph = sorted(phone_book)

    for i in range(len(ph)-1):
        if len(ph[i]) < len(ph[i+1]):
            if ph[i] == ph[i+1][:len(ph[i])]:
                answer = False
                break

    return answer


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
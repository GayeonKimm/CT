def solution(phone_book):
    answer = True
    print("sort 전 phone_book = ",phone_book)
    phone_book.sort()
    print("sort 후 phone_book = ",phone_book)

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break   #하나만 있어도 False니까 break

    return answer


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
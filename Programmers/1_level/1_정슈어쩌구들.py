# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    return answer[::-1]
print(solution(123456))


# 자릿수 더하기
def solution1(n):
    answer = [int(i) for i in str(n)]
    return sum(answer)
print(solution1(123))


# 제일 작은수 제거하기 -- 4점은 받음 이것도
# def solution2(arr):
#     if len(arr) == 1:
#         return [-1]
#     a = min(arr)
#     arr.remove(a)
#     return arr

def solution2(arr):
    answer = [i for i in arr if i > min(arr)]
    if len(answer) == 0:
        return [-1]
    else:
        return answer
print(solution2([4,3,2,1]))
print(solution2([10]))

# 정수 내림차순으로 배치하기
def solution3(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    return int(''.join(answer))
print(solution3(118372))


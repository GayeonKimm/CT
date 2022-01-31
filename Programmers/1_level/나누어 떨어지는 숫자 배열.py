def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer


arr, divisor = [1,3,5,10,15], 5
print(solution(arr, divisor))



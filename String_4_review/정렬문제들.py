'''
맨 앞자리 수로 정렬을 수행해야할 때
'''

def solution(numbers):
    numbers.sort(key= lambda x:str(x)*333, reverse=True)
    if numbers[0] == 0:
        return '0'
    else:
        return "".join(map(str, numbers))


# H- index
# 이해 잘 안됨 ;;

def solution(citations):
    answer = 0
    c  = sorted(citations, reverse= True)
    for i in range(len(c)):
        if i + 1 <= c[i]:
            answer = i+1
    return answer
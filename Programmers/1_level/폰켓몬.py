def solution(nums):
    # nums는 항상 짝수로 주어진다는 조건 존재.
    n = len(nums)/2
    new_nums = set(nums)  # 여기까지만 해도 되더라고. list안해도
    if n > len(new_nums):
        return len(new_nums)
    else:
        return int(n)
        #소수점 나오길래 int 씌웠음

# nums = [3,1,2,3]
nums = [1,2,3,4,5,5]
print(solution(nums))
# 재풀이 +12. int 처리 해야 7,8,9 테케 오류 안남
'''
1. 숫자를 이진법으로 변경하기 0을 하나씪 추가하는게 좋음
2. 짝수는 마지막이 0 으로 무조건으로 끝나고, 그숫자 1 로 바꾸면 정답임
3. 홀수는
- 0 이 있는 자리수에서 1로 변경
- 그 다음수를 0으로 변경하면 제일 작은수가 됨

* 문제에 양의 정수라고 주어졌지만 처음에 int 처리 안하면 정답처리 안됨ㅜ
'''

def solution(numbers):
    answer = []
    for i in numbers:
        bnum = list('0' + bin(int(i))[2:])
        idx = ''.join(bnum).rfind('0')
        bnum[idx] = '1'

        if i % 2 == 1:
            bnum[idx+1] = '0'

        answer.append(int(''.join(bnum), 2))
    return answer

numbers = [2,7]
print(solution(numbers))
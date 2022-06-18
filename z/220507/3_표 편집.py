'''
힙 문제인가?
1 ~ 8 적어두고
삭제된거는 temp에 저장해두고 하나씩 불러오면 되니까
그리고 마지막에는 숫자 비교해서 확인하는겨

- range 조절 해야될 거 같어
'''
import heapq
def solution(n, k, cmd):
    excel = [i for i in range(n)]
    now = k
    temp = [] # 삭제된 거 담아 놓는
    for i in cmd:
        if len(i) > 1:
            cm, cnt = i.split()
            if cm == 'U': # 올라가
                now -= int(cnt)
            elif cm == 'D': # 내려가
                now += int(cnt)
        else:
            if i == 'C':
                temp.append(excel[now + 1])
                excel.remove(now)
            elif i == 'Z':
                heapq.heappush(excel, temp[-1])
    # 비교
    first = [i for i in range(1, n+1)]
    answer = ''
    for f, e in zip(first, excel):
        if f == e:
            answer += '0'
        else:
            answer += 'X'
    return answer


n, k, cmd = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# n, k, cmd = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n,k,cmd))
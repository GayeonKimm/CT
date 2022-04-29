'''
6점 받음

1. 숫자인지만 판단해버리면 그 뒤로는
그 처음으로 숫자 나오는 인덱스 찾아서!!
index인가 그거
나누면 될 거 같은데 말야
-> 걍 숫자 나오면 그 뒤 문자로 다시 for 문 실행!!!!!!!!
** if not**

- sort
- join
answer에 저장해두면 한번에 어케 출력하는데?
join하는 방법밖에 없나 -> 네~!

'''
def solution(files):
    answer = []
    for file in files:
        head, number, tail = '','',''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                answer.append([head, number,tail])
                break
    answer.sort(key = lambda x :(x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

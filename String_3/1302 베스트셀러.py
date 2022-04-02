'''
Counter로 할까 dictionary로 할까
사실 뭐하나 능숙하게 할 줄 아는 것은 없음
'''
# 1 counter
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
books = []
for _ in range(n):
    books.append(input().strip())
books.sort() # 이거 안하면 틀림
counter = Counter(books)
print(counter.most_common(n=1)[0][0])

#2. dictionary
n = int(input())
books = {}
for _ in range(n):
    book = input().strip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
max_cnt = max(books.values())
answer = []
for b, n in books.items():
    if n == max_cnt:
        answer.append(b)
print(sorted(answer)[0])

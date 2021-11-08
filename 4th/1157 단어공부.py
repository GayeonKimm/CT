# 슬슬 하기 싫다
# 입력 받은거 따로 두고, set한거 따로 두고,
# 원래 입력에서 count 세서 cnt만들어 둔 다음에
# cnt의 최대값인거 인덱스를 set한 리스트에서 찾기 . upper로 print

word = input().upper()
word_list = list(set(word))
cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)
# print(cnt)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))])

# 개짜증나네 왜 백준 틀렸다고 하지?
# 가연아 print를 넣고서 틀렸다고 화를 내면 어떡하니
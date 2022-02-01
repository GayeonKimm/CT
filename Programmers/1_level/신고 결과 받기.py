from collections import Counter
def solution(id_list, report, k):
    answer = []
    chk = []

    dic = {}
    for i in id_list:
        dic[i] = []

    for case in report:
        report_id, report_name = case.split()
        if report_name not in dic[report_id]:
            dic[report_id].append(report_name)
            chk.append(report_name)

    counter = Counter(chk)

    for report_id in id_list:
        a = [i for i in dic[report_id] if counter[i] >= k]
        answer.append(len(a))

    return answer


# id_list, report, k = ["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"], 3
id_list, report, k = ["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2
print(solution(id_list, report, k))
#https://somjang.tistory.com/entry/Programmers-2022-KAKAO-BLIND-RECRUITMENT-%EC%8B%A0%EA%B3%A0-%EA%B2%B0%EA%B3%BC-%EB%B0%9B%EA%B8%B0-Python
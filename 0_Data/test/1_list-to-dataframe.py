'''
리스트를 dataframe으로, pivot으로, 결과를 flatten 으로
pivot에서 리스트 중복값이 존재하면 ValueError 발생

1. 주어진 데이터를 각 컬럼별 리스트를 만들어서 넣어두기
2. 넣어둔 리스트를 데이터 프레임으로
3. 피벗테이블로
4. flatten의 리스트로
'''

import numpy as np
import pandas as pd

def solution(data):
    fruits = []
    name = []
    count = []
    for i in data:
        fruits.append(i[0])
        name.append(i[1])
        count.append(i[2])
    # 각각의 리스트로 저장시켜 둠

    data_df = pd.DataFrame({'과일': fruits, '이름': name, '개수': count})
    data_pv = pd.pivot(data_df, '과일', '이름', '개수')
    print(data_pv)

    answer = np.array(data_pv).flatten().tolist()
    return answer

data = [['Apple', '가', 1], ['banana', '가', 1], ['strawberry', '가', 3],
        ['Apple', '나', 3], ['banana', '나', 2], ['strawberry', '나', 1],
        ['Apple', '다', 1], ['banana', '다', 2], ['strawberry', '다', 2],
        ['Apple', '라', 2], ['strawberry', '라', 9]]
print(solution(data))
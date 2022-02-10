# 자전거 수요 예측
#1. 필요한 라이브러리
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import scipy

# 2 데이터 불러오기
train = pd.read_csv('dataset/train.csv')
test = pd.read_csv('dataset/test.csv')
submission = pd.read_csv('dataset/sampleSubmission.csv')

# 3 데이터 확인
print(train.columns)
print(test.columns)
#  train에는 casual, registered, count가 없음
# test에서 count를 예측해야됨
# count = registered + casual 이므로

# 데이터의 datetime을 날짜로 인식해주기 위해
train['datetime'] = pd.to_datetime(train['datetime'])
test['datetime'] = pd.to_datetime(test['datetime'])
print(train.head())
print(train.info()) # 변경되었음을 확인

print(train.shape)
print(test.shape)
# (10886, 12)
# (6493, 9)

# 4 데이터 EDA 진행
# 데이터를 시각화하고, null값을 처리하는 모델링을 위한 사전 준비

##1 기준별 자전거 수요랑 확인해보기 (시각화)
# yyyy-mm-dd 00:00:00 을 년, 월, 일, 시, 분, 초로 나눠서 자전거 수요량 확인
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second

# dayofweek 은 요일을 가져옴.
# 월 : 0 1,2,3,4,5, 일:6

train['dayofweek'] = train['datetime'].dt.dayofweek
#
## test도 동일하게 진행
# 이때 test datetime 으로 변경했는지 확인
test['year'] = test['datetime'].dt.year
test['month'] = test['datetime'].dt.month
test['day'] = test['datetime'].dt.day
test['hour'] = test['datetime'].dt.hour
test['minute'] = test['datetime'].dt.minute
test['second'] = test['datetime'].dt.second
test['dayofweek'] = test['datetime'].dt.dayofweek

## 연도별 자전거 수요량
# sns.barplot(data=train, x='year', y='count')
# plt.show() # 파이참에서 그림 확인할 수 있음
# 자전거 수요가 늘었다. 2012년에도 늘었으니 앞으로도 늘 가능성이 있다.
# 예측함에 있어서 year를 사용할 수 있겠다
# sns.barplot(data=train, x='month', y='count')
# sns.barplot(data=train, x='day', y='count')

## season별 자전거 수요량
# sns.barplot(data=train, x = 'season',y='count')
# plt.show()

# month로 확인했을 때는 겨울에 소비가 적었는데 이 그래프에서는 다르게 나왔네
print(train[train['season'] == 1].month.unique())
print(train[train['season'] == 2].month.unique())
print(train[train['season'] == 3].month.unique())
# season이 1인 경우의 month들의 값들은 1,2,3월


## 시간대별 point plot
# fig, ax1 = plt.subplot(1,1)
# fig.set_size_inches(20, 5) # 가로,세로
# 이게 그래프 크기 같은거 설정하는거 같은데 자꾸 오류나서....

# sns.pointplot(data = train, x = 'hour', y = 'count')
# 8시, 17시, 주로 출퇴근 시간대에 자전거 많이 사용


## workingday - 카테고리형 시간대별로 pointplot 확인
# sns.pointplot(data = train, x = 'hour', hue='workingday', y = 'count')
# 근무날 아닐때는 오후시간대에 수요량이 더 높다
# hoilday도 count 변수 예측에 영향을 주겠군

## holiday- 카테고리형 시간대별로 pointplot 확인
# sns.pointplot(data = train, x = 'hour', hue='holiday', y = 'count')
# 휴일에는 오후 시간대에 증가하네 holiday도 변수 예측에 사용하면 좋겠다.


## weather- 카테고리 시간대별로 pointplot 확인
# sns.pointplot(data=train, x = 'hour',y='count',hue='weather')
# 4번의 최악의 날씨엔 거의 데이터가 없음

## dayofweek - 카테고리, 시간대별로 pointplot 확인
# sns.pointplot(data=train, x = 'hour', y='count', hue='dayofweek')


# year, month, day, hour, weather, holiday, workingday, dayofweek, season

# 변수끼리의 상관관계
# 앞에 train 안써서 개난리남.
corr_data = train[['datetime', 'season', 'holiday', 'weather', 'temp', 'atemp', 'humidity', 'windspeed']]
colormap = plt.cm.PuBu

# sns.heatmap(corr_data.corr(), linewidths=0.1, square=True, annot=True, cmap=colormap)
# temp와 atemp의 상관관계가 매우 높아서 다중공선성이 의심되므로 temp 변수 하나만 사용할거여


## 온도, 습도, 바람세기에 대해 살펴보기

# fig, (ax1, ax2, ax3) = plt.subplots(ncols = 3, figsize=(12,5))

# sns.scatterplot(data = train, x = 'windspeed', y = 'count', ax = ax1)
# sns.scatterplot(data = train, x = 'temp', y = 'count', ax = ax2)
# sns.scatterplot(data = train, x = 'humidity', y =  'count', ax = ax3)
# 바람세기가 0인 경우는 거의 없기 때문에 windspeed 변수의 0이 많음

print(len(train[train['windspeed'] == 0]))
# 10000개의 데이터에서 1313개는 많다고 판단. windspeed 가 0인 것을 대체하는
# feature engineering 과정이 하나 더 필요함




"""
Feature Engineering
1. 데이터의 왜도와 첨도를 살펴보고 조절해줄것
2. IQR 방법으로 이상치를 제거해 
3. 그리고 feature engineering 진행할 것
"""

# 1. 이상치 제거
# 연속형 변수에 대한 boxplot 작성 및 이상치 확인
# fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(nrows = 6, figsize = (12,10))
# sns.boxplot(data = train, x = 'windspeed', ax = ax1)
# sns.boxplot(data = train, x = 'humidity', ax = ax2)
# sns.boxplot(data = train, x = 'temp', ax = ax3)
# sns.boxplot(data = train, x = 'casual', ax = ax4)
# sns.boxplot(data = train, x = 'registered', ax = ax5)
# sns.boxplot(data = train, x = 'count', ax = ax6)
# plt.show()


# 이상치 제거를 위한 함수 작성
from collections import Counter
def detect_outliers(data, n, cols):
    outlier_indices = []

    for col in cols:
        Q1 = np.percentile(data[col], 25)
        Q3 = np.percentile(data[col], 75)
        IQR = Q3 - Q1

        outlier_step = 1.5 * IQR

        outlier_list_col = data[(data[col] < Q1 - outlier_step) | (data[col] > Q3 + outlier_step)].index
        outlier_indices.extend(outlier_list_col)
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.items() if v > n)

    return multiple_outliers

Outliers_to_drop = detect_outliers(train, 2, ["temp", "atemp", "casual", "registered", "humidity", "windspeed", "count"])

train = train.drop(Outliers_to_drop, axis=0).reset_index(drop=True)
print(train.shape)

# 이상치 제거 완

# 2 왜도와 첨도 확인
# fig, ax = plt.subplot(1,1, figsize = (10,6))
# graph = sns.distplot(train['count'], color='b', label='Skewness:{:2f}'.format(train['count'].skew()))
# graph = graph.legend(loc='best')
# print('skewness(왜도): %f' %train['count'].skew())
# print('kurtosis(첨도): %f' %train['count'].kurt())
# plt.show()

#lambda 를 사용해서 로그를 취해준 count값을 count_log 컬럼으로 생성해주자
train['count_log'] = train['count'].map(lambda i:np.log(i) if i > 0 else 0)

# fig, ax = plt.subplots(1,1, figsize = (10, 6))
# graph = sns.distplot(train['count_log'], color = 'b', label = 'skewness: {:2f}'.format(train['count_log'].skew()), ax = ax)
# graph = graph.legend(loc = 'best')
#
# print("skewness(왜도): %f" %train['count_log'].skew())
# print("kurtosis(첨도): %f" %train['count_log'].kurt())

#필요없는 count값 없애주기
train.drop('count', axis = 1, inplace = True)
# plt.show()


## windspeed = 0 대체값 찾기

# 예측된 값으로 대체하는 방법으로 0을 바꿔주고자 한다.

# randomForest를 활용해 예측값으로 windspeed = 0.0 값을 대체하기
from sklearn.ensemble import RandomForestClassifier
def predict_windspeed(data):
    wind0 = data.loc[data['windspeed'] == 0]
    windnot0 = data.loc[data['windspeed'] != 0]

    # 풍속이 날씨변수이기 때문에 날씨변수를 활용해서 windspeed를 예측해줄 것
    col = ['season', 'weather', 'temp', 'humidity', 'atemp', 'day']

    windnot0['windspeed'] = windnot0['windspeed'].astype('str')

    rf = RandomForestClassifier()
    # windspeed가 0이 아닌 컬럼으로 fit 해줌
    # model.fit(X_train, y_train)
    rf.fit(windnot0[col], windnot0['windspeed'])

    # windspeed가 0인 부분을 예측
    # model.predict(X_test)
    pred_wind0 = rf.predict(X=wind0[col])

    # wind0의 windspeed 값을 pred_wind0으로 바꿔주고
    wind0['windspeed'] = pred_wind0

    # windnot0과 wind0을 합쳐준다
    data = windnot0.append(wind0)
    data['windspeed'] = data['windspeed'].astype('float')

    data.reset_index(inplace=True)
    data.drop("index", inplace=True, axis=1)

    return data

train = predict_windspeed(train)
test = predict_windspeed(test)

print(train[train['windspeed']== 0.0])
# 없다

# train과 test의 시각화

#갯수를 세야하니 countplot
fig, (ax1, ax2) = plt.subplots(2,1)
sns.countplot(data = train, x = 'windspeed',ax = ax1)
sns.countplot(data = test, x = 'windspeed', ax = ax2)
# plt.show()


# one-hot encoding 범주형 변수 처리
# season, holiday, workingday, weather

train = pd.get_dummies(train, columns=['weather'],prefix ='weather')
test = pd.get_dummies(test, columns=['weather'], prefix='weather')

train = pd.get_dummies(train, columns =['season'], prefix='season')
test = pd.get_dummies(test, columns=['season'], prefix = 'season')

train = pd.get_dummies(train, columns = ['holiday'], prefix = 'holiday')
test = pd.get_dummies(test, columns = ['holiday'], prefix = 'holiday')

print(train.columns)
print(test.columns)

"""
Modeling
train에 사용될 변수를 선택하자
위의 columns 내역을 보고 drop할 컬럼을 선택해주었다.

submission의 형태를 살펴보았을 때, datetime을 기준으로 예측값을 적었다.
따라서 test의 datetime은 미래의 submission을 위해서 따로 저장해두기로 한다
"""

test_datetime = test['datetime']

train.drop(['datetime', 'workingday', 'atemp', 'registered', 'casual', 'minute', 'second'], axis=1, inplace=True)
test.drop(['datetime', 'workingday', 'atemp', 'minute', 'second'], axis=1, inplace=True)

"""
workingday는 holiday와 너무 비슷한 양상을 띄고 있어서 working삭제 
temp와 atemp 상관관계 높아서 atemp삭제 
year 등의 시간 변수 존재하니까 datetime 삭제 
초,분은 필요없어서 삭제
"""
print(train.columns)
print(test.columns)

"""
Gradient Boosting 모델 학습
1. 데이터 셋 분할"""
from sklearn.model_selection import train_test_split
from sklearn import metrics

# 데이터 프레임 형태가 아닌 array여야 하기 떄문에 values
X_train = train.drop('count_log', axis=1).values
target_label = train['count_log'].values
X_test = test.values
X_tr, X_val, y_tr, y_val = train_test_split(X_train, target_label, test_size=0.2, random_state=2000)

# print(X_tr, X_val, y_tr, y_val)


# 모델링 학습
# gradient boosting 모델

from sklearn.ensemble import GradientBoostingRegressor
regressor = GradientBoostingRegressor(n_estimators=2000, learning_rate = 0.5,
                                      max_depth=5, min_samples_leaf=15,
                                      min_samples_split=10, random_state=42)

# model.fit(x,y)
regressor.fit(X_tr, y_tr)


# 모델 성능 평가
score_train = regressor.score(X_tr, y_tr)
score_val = regressor.score(X_val, y_val)
print("trian score : %f" %score_train)
print('validation score : %f' %score_val)

"""
예측 및 submission.csv 생성
1. 예측
앞서 만든 regressor 모델에 x_test 데이터를 넣어 예측 수행"""
pred = regressor.predict(X_test)


# 2 파일 생성
sample = pd.read_csv('dataset/sampleSubmission.csv')
print(sample.head())
# 불러와서 확인 좀 하고

submission = pd.DataFrame()
submission['datetime'] = test_datetime
submission['count_log'] = pred

submission['count'] = np.exp(submission['count_log'])
submission.drop('count_log', axis = 1, inplace=True)
print(submission.head())



# 마지막 엑셀로 내보내기
# submission.to_csv("Bike.csv", index = False)

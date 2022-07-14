# id : 샘플 아이디
# Store : 쇼핑몰 지점
# Date : 주 단위(Weekly) 날짜
# Temperature : 해당 쇼핑몰 주변 기온
# Fuel_Price : 해당 쇼핑몰 주변 연료 가격
# Promotion 1~5 : 해당 쇼핑몰의 비식별화된 프로모션 정보
# Unemployment : 해당 쇼핑몰 지역의 실업률
# IsHoliday : 해당 기간의 공휴일 포함 여부
# Weekly_Sales : 주간 매출액 (목표 예측값)

# 데이터를 불러오고 살펴보기 위한 pandas 라이브러리
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, cross_validate
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, PowerTransformer, RobustScaler, StandardScaler

# train 데이터 불러오기
train = pd.read_csv('shop1/train.csv')

# test 데이터 불러오기
test = pd.read_csv('shop1/test.csv')

# sample_submission 불러오기
sample_submission = pd.read_csv('shop1/sample_submission.csv')

print(train.info()) # null값 대신 nan으로 대체, date 2010년 2월 5일 부터 2012년 9월 28일
print(train.describe()) # id는 6255개 , 지점종류는 1-45까지, 온도는 -2도~100도, 연료값 2.47~4.3, 프로모션....,실업률 4.07~14.31

# import matplotlib.pyplot as plt
# # 이번엔 예측하고자 하는 값인 Weekly_Sales를 확인해봅니다.
# plt.hist(train.Weekly_Sales, bins=50)
# plt.show()

# 결측치 처리 - promotion에서 0으로 처리하기
train = train.fillna(0)
test=test.fillna(0)

##### 전처리
# Date 칼럼에서 "월"에 해당하는 정보만 추출하여 숫자 형태로 반환하는 함수를 작성합니다.
def get_month(date):
    month = date[3:5]
    month = int(month)
    return month
def get_day(date):
    day = date[0:2]
    day = int(day)
    return day
def get_year(date):
    year = date[6:]
    year = int(year)
    return year

# 이 함수를 Date 칼럼에 적용한 Month 칼럼을 만들어줍니다.
train['Day'] = train['Date'].apply(get_day)
train['Month'] = train['Date'].apply(get_month)
train['Year'] = train['Date'].apply(get_year)
test['Day'] = test['Date'].apply(get_day)
test['Month'] = test['Date'].apply(get_month)
test['Year'] = test['Date'].apply(get_year)

# IsHoliday 칼럼의 값을 숫자 형태로 반환하는 함수를 작성합니다.
def holiday_to_number(isholiday):
    if isholiday == True:
        number = 1
    else:
        number = 0
    return number

# 이 함수를 IsHoliday 칼럼에 적용한 NumberHoliday 칼럼을 만들어줍니다.
train['NumberHoliday'] = train['IsHoliday'].apply(holiday_to_number)
test['NumberHoliday'] = test['IsHoliday'].apply(holiday_to_number)


# 분석할 의미가 없는 칼럼을 제거합니다.
train = train.drop(columns=['id','Date'])
test = test.drop(columns=['id','Date'])
# 학습에 사용할 정보와 예측하고자 하는 정보를 분리합니다.
data = train.drop(columns=['Weekly_Sales']) # real train data
label = train[['Weekly_Sales']] # label

## 스케일링
def find_best_scaler(train_x, test_x, train_y):
    best_score = 100
    columns = train_x.columns
    for scaler in [PowerTransformer(), MinMaxScaler(), StandardScaler(), MaxAbsScaler(), RobustScaler()]:        
        scaled_train_x = scaler.fit_transform(train_x)
        scaled_train_x = pd.DataFrame(scaled_train_x, columns = columns).astype('float64')
        train1=scaled_train_x.to_numpy()
        print(train1)
        scaled_test_x = scaler.transform(test_x)
        scaled_test_x = pd.DataFrame(scaled_test_x, columns = columns).astype('float64')
        test1=scaled_test_x.to_numpy()
        print(test1)
        print(train_y.to_numpy())
        skf = StratifiedKFold(n_splits=3 , shuffle=True)
        rf = RandomForestClassifier()
        scores = [abs(x) for x in cross_validate(rf, train1, train_y.to_numpy(), cv=skf)]
        print(scaler.__class__.__name__)
        print(f'TOTAL 최대성능: {min(scores)}\n평균성능: {np.mean(scores)}')
        print('-'*30)
        
        if np.mean(scores) < best_score:
            best_score = np.mean(scores)
            best_train_x = scaled_train_x
            best_test_x = scaled_test_x
            best_scaler = scaler
    
    print('BEST SCALER : ', best_scaler.__class__.__name__)
    
    return best_score, best_train_x, best_test_x, best_scaler

print(label)

_, scaled_train_x, scaled_test_x, scaler = find_best_scaler(data,test, label)



final_train_x=scaled_train_x
final_test_x=scaled_test_x

from sklearn.linear_model import LinearRegression
# 모델 선언
model = LinearRegression()
# 모델 학습
model.fit(final_train_x,label)
# 학습된 모델을 이용해 결과값 예측후 상위 10개의 값 확인
prediction = model.predict(final_test_x)
score=model.score(final_train_x,label)
print('----------------------예측된 데이터의 상위 10개의 값 확인--------------------\n')
print(prediction[:10])

sample_submission['Weekly_Sales'] = prediction
sample_submission.to_csv('shop1/sample_submission1.csv',index = False)
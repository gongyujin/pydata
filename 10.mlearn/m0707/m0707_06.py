from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split # train, test
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor


# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15 # 상단제목 글자 15크기 변환
matplotlib.rcParams['axes.unicode_minus']=False # 눈금 -표시 처리
# matplotlib.rcParams['font.family']='Apple Gothic' # 맥사용시


# 데이터 불러오기
picher=pd.read_csv('10.mlearn/m0707/picher_stats_2017.csv')
picher2=pd.read_csv('10.mlearn/m0707/picher_stats_2017.csv')

#---------------------------------------
# 컬럼구성에 대한 출력
# ['선수명', '팀명', '승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
#        '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
#        '연봉(2018)', '연봉(2017)']
# print(picher.columns)
label=picher['연봉(2018)']
#----------------------------------------

#----------------------------------------
# # 그래프 출력
# plt.hist(label,bins=100)
# picher.boxplot(column=['연봉(2018)'])
# plt.scatter(picher['선수명'],picher['연봉(2018)'])
# plt.show()

# 데이터 전처리
# print(picher.describe()) # 정규화, 표준화작업이 필요
# print(picher.info()) # null 값이 있는지 확인해보기, type 확인하기
picher_features_df=picher[[
    '승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
    '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
    '연봉(2018)', '연봉(2017)']]
#----------------------------------------
#----------------------------------------
# # 컬럼전체를 1개씩 그래프 출력
# def plot_hist(df):
#     plt.rcParams['figure.figsize']=[20,16]
#     fig=plt.figure(1)
#     # 5*5
#     for i in range(len(df.columns)):
#         ax=fig.add_subplot(5,5,i+1)
#         plt.hist(df[df.columns[i]],bins=50)
#         ax.set_title(df.columns[i])    
#     plt.show()
    
    
# plot_hist(picher_features_df)
# print(picher[picher.columns[0]]) # 선수명
#----------------------------------------

# 정규화, 표준화작업
# (데이터-평균)/표준편차
# 함수생성 : 전체데이터, 전체 컬럼리스트 개수
def standard_scaling(df,scale_columns):
    for col in scale_columns:
        series_mean=df[col].mean() # 평균
        series_std=df[col].std() # 표준편차
        # (데이터-평균)/표준편차
        df[col]=df[col].apply(lambda x:(x-series_mean)/series_std)
    return df

scale_columns=['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
    '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
    '연봉(2017)']

# 정규화, 표준화 완료
# print(picher['연봉(2018)'])
picher_df=standard_scaling(picher,scale_columns)
# print(picher_df)

# 컬럼명 변경 - 컬럼 22개
picher_df=picher_df.rename(columns={'연봉(2018)':'y'})

# 팀명 원핫인코딩 : 팀명을 숫자로 변경 - 9개 컬럼
team_encoding = pd.get_dummies(picher_df['팀명'])
picher_df=picher_df.drop('팀명', axis=1) # 컬럼 21개
picher_df=picher_df.join(team_encoding) # 컬럼 30개

# 알고리즘 선택
lr=LinearRegression()
# RandomForestRegressor
# KNeighborsRegressor

# 데이터 분리
# 컬럼중 선수명,y를 제외하고 모든 컬럼 가져오기
data=picher_df[picher_df.columns.difference(['선수명','y'])]
label=picher_df['y']
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 훈련
lr.fit(train_data,train_label)

# 정확도
print(lr.score(train_data,train_label))
print(lr.score(test_data,test_label))

# # picher에서 컬럼의 영향력 파악분석
# scale_columns=['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
#     '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
#      '연봉(2017)']

# corr=picher_df[scale_columns].corr(method='pearson')
# show_cols=['win','lose','save','hold','blon','match','start',
#            'inning','strike3','ball4','homerun','babip','lob','era',
#            'ra9-war','fip','kfip','war','2017']

# hm=sns.heatmap(corr.values,
#                cbar=True,
#                square=True,
#                annot=True,
#                fmt='.2f',
#                annot_kws={'size':15},
#                yticklabels=show_cols,
#                xticklabels=show_cols)
# plt.tight_layout()
# plt.show()

# 첫번재 컬럼 : vif, 두번째 컬럼 : 컬럼명 출력
vif = pd.DataFrame()
vif['VIF factor'] = [variance_inflation_factor(data.values,i) for i in range(data.shape[1])]
vif['features']=data.columns
# print(vif.round(1))

# ----------------------------------------------------
# 너무 영향력이 높거나, 너무 낮은 것을 파악해서
# 다시 훈련을 실시 함.
# ----------------------------------------------------

x=picher_df[['FIP','WAR','볼넷/9','삼진/9','연봉(2017)']]
y=picher_df['y']
train_data,test_data,train_label,test_label=train_test_split(x,y,random_state=42)

lr=LinearRegression()
lr.fit(train_data,train_label)

print('재설정 train score : ',lr.score(train_data,train_label))
print('재설정 test score : ',lr.score(test_data,test_label))

# vif = pd.DataFrame()
# vif['VIF factor'] = [variance_inflation_factor(x.values,i) for i in range(x.shape[1])]
# vif['features']=x.columns
# print(vif.round(1))

# 예측
predict_2018_salary=lr.predict(x)
picher2=pd.read_csv('10.mlearn/m0707/picher_stats_2017.csv')
picher2['예측연봉(2018)']=pd.Series(predict_2018_salary)

# def re_scaling(df,scale_columns):
#     for col in scale_columns:
#         series_mean=df[col].mean() # 평균
#         series_std=df[col].std() # 표준편차
#         # (데이터-평균)/표준편차
#         df[col]=df[col].apply(lambda x:(x-series_mean)/series_std)
#     return df

# scale_columns=['선수명', '팀명', '승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
#     '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
#     '연봉(2018)', '연봉(2017)']

# # 정규화, 표준화 완료
# # print(picher['연봉(2018)'])
# picher_df=standard_scaling(picher,scale_columns)


# # 예측연봉 출력
# result_df=picher_df.sort_values(by=['y'],ascending=False)


print(picher2[['연봉(2017)','연봉(2018)','예측연봉(2018)']])

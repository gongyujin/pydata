import pandas as pd

# excel 파일 불러오기
df=pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)
print(df.iloc[0]) # rows index 출력
print(df.index)  # index지정 모두 출력
print(df.index[3]) # index지정 3번째 출력 => 4번
print(df.loc['2번']) # rows index명으로 출력
print(df.loc[df.index[3]]) # rows index명으로 출력 => 지원번호 4번에 대한 정보를 가져옴

# # 숫자컬럼 최대값, 평균, 숫자분포도 통계를 보여줌
# print(df.describe())

# # 각 컬럼의 타입을 알려줌
# print(df.info())

# df=pd.read_excel('user.xlsx')
# print(df)
# # 컬럼 타입정보 - object, float, int
# print(df.info())

# # 상위 5개만 보여짐
# print(df.head())
# # 상위 10개 보여줌
# print(df.head(10))

# # 하위 5개만 보여짐
# print(df.tail())
# # 하위 20개 보여줌
# print(df.tail(20))

# print(df.values) # 배열구조로 출력 (리스트 형태)
# print(df.values[500:505])
# arr=df.values[0]
# print(type(arr))

# print(df.iloc[0]) # 1개 row출력
# print(df['first_name']) # 1개 col출력
# print(df[['first_name','gender']]) # 2개 col출력

# print(df.index) # index 출력
# print(df.columns) # 컬럼출력
# print(df.shape) # row, column 수를 출력

# skiprows: 개수만큼 제외, nrows: 개수만큼 가져옴
df=pd.read_excel('user.xlsx')
print(df)
df=pd.read_excel('user.xlsx',skiprows=[i for i in range(0,500)],nrows=10)
print(df)
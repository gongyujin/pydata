import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# # '키'를 기준으로 순차정렬
# print(df.sort_values('키'))

# # 키를 기준으로 역순정렬
# print(df.sort_values('키',ascending=False))

# 수학, 영어를 기준으로 정렬
# 수학으로 먼저 순차정렬하고, 같은 점수만 영어로 다시 순차정렬
print(df.sort_values(['수학','영어']))
# 역순정렬 수학점수가 같을경우, 영어기준으로 정렬
print(df.sort_values(['수학','영어'],ascending=False))

# 수학은 역순정렬, 영어는 순차정렬
print(df.sort_values(['수학','영어'],ascending=[False,True]))

# # index기준으로 역순정렬
# print(df.sort_index(ascending=False))


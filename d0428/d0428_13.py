# 연령별인구현황 여자부분 출력
# 행정기관, 0~4세, .... ,100세이상까지 출력
# 제일 마지막 컬럼 1개 : 100세이상의 합계를 구하시오.

import pandas as pd

df_m=pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3, usecols='B,E:Y')

# print(df_m.columns)
df_m.set_index('행정기관',inplace=True)
# print(df_m)
print(df_m.index)

df_m.rename(index={'전국  ':'전국'},inplace=True)
print(df_m.index)

# df_w=pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,usecols='B,AB:AV')
# # print(df.columns.values)
# print(df_w)
# df_w[df_w.columns[-1]]=df_w[df_w.columns[-1]].str.replace(',','').astype(int)
# print('100세 이상 합계 : {:,d}'.format(df_w[df_w.columns[-1]][1:].sum()))

# print(df_w.columns)
# df_w.columns=df_m.columns
# print('-'*50)
# print(df_w.columns)


# # 컬럼명 변경
# df.rename(columns={'100세 이상.1':'100세 이상'},inplace=True)
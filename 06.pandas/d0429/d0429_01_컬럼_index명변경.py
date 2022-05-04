import pandas as pd

df_m=pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,usecols='B,E:Y',index_col='행정기관')
df=pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,usecols='B,AB:AV',index_col='행정기관')
print(df.columns)


# 컬럼 title 전체를 변경
df.columns=df_m.columns
print(df.columns)

# df.columns[0]= '4세' # rename으로 바꿔야함 이렇게는 바꿀 수 없음
# 1개 컬럼 title명을 변경 == > rename
df.rename(columns={df.columns[0]:'4세'},inplace=True)
print(df.columns)
print(type(df.columns[0]))


for i in range(len(df.index)):
    # 빈공백 제거 : strip()
    # re.sub(korean,'',str) # 한국어 제거
    df.rename(index={df.index[i]:df.index[i].strip()},inplace=True)
    
# df.rename(index={'전국  ':'전국'},inplace=True)
print(df.index.values)
print(len(df.index))

# df=pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,usecols='B,E:Y',index_col='행정기관')
# print(df)

# print(df.columns)

# print(df['0~4세'])
# # pandas 1차원 데이터 여러개
# print(type(df['0~4세']))
# df['0~4세']=df['0~4세'].str.replace(',','').astype(int) # series를 string으로 변환시켜줌, int로 변환
# print(df['0~4세'][1:].sum())


# # string형
# print(type(df['0~4세'][0]))
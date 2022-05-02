import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# column수정
# # 1. 컬럼의 데이터를 비교해서 컬럼의 값을 변경하는 방법
# df['학교'].replace({'구로고':'단지고','디지털고':'상생고'},inplace=True) # 전체 이름을 변경할때 replace를 사용함 
# df['국어'].replace({100:190},inplace=True)

# # 2. 컬럼전체를 변경 - 전체 소문자 변경
# df['SW특기']=df['SW특기'].str.lower() #소문자
# df['SW특기']=df['SW특기'].str.upper() #대문자
# df['SW특기']=df['SW특기'].str.capitalize() #첫글자만 대문자

# df['SW특기']='합격' # 한번에 전체 변경
# df['SW특기'].replace({'Java':'javaC'},inplace=True)

# df['학교']=df['학교']+'등학교'

# 키 180 + cm 
# 타입이 다를경우 에러 : +가 되지 않음, 형변화를 해줘야함, astype함수
df['키']=df['키'].astype(str)+'cm'
print(df)

# # 3. 다른 컬럼의 값을 비교해서 컬럼의 데이터를 변경
# filt=df['키']>=190
# df.loc[filt,'국어']=100

# # row index를 가지고 row데이터 수정
# df.loc['4번','SW특기']='PYTHON'
# # row의 2개 컬럼값을 변경
# df.loc['4번',['학교','SW특기']]=['가산고','PYTHON']

# # 1. 강태원 국어점수 40 -> 50
# df.loc['2번','국어']=50
# # 2. 국어점수가 40점 -> 50
# df['국어'].replace({40:50},inplace=True)

# # 3. 강태원 -> 국어점수가 40점이면 영어,수학,과학,사회 모두 40점
# filt=(df['국어']==40) & (df['이름']=='강태원')
# df.loc[filt,['영어','수학','과학','사회']]=[40,40,40,40]

# print(df)


# column추가
# 추가 - 새로운컬럼 title이 입력되면 추가 됨, 새로운 row index가 입력되면 추가 됨
# df.loc['9번']=['이순신','디지털고',200,100,100,100,90,80,'python'] # 컬럼 개수를 맞추지 않으면 에러가 발생함
# df['총합']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
# print(df)
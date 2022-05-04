# [ 문제 1] stu1000.csv 파일 읽어와서, 학교컬럼변경 : 1-구로고, 2-디지털고, 3-단지고
# SW특기 : 1-Java, 2-c, 3-Python 4-Javascript 5-JAVA 변경하시오.
import pandas as pd

def school(temp):
    if temp==1:
        result='구로고'
    elif temp==2:
        result='디지털고'
    else:
        result='단지고'
    return result

def SW(temp):
    if temp==1:
        result='Java'
    elif temp==2:
        result='c'
    elif temp==3:
        result='Python'
    elif temp==4:
        result='Javascript'
    else:
        result='JAVA'
    return result

df=pd.read_excel('stu1000.xlsx')
df['학교']=df['학교'].apply(school)
df['SW특기']=df['SW특기'].apply(SW)
print(df)



# [ 문제 2 ] stu1000 합계, 평균, 평가 컬럼을 추가하시오. ( 합계 : 국어,영어,수학,과학,사회 점수 합
# 평균 : 합계/5, 평가 90이상A, 80점이상B,70점이상C,60점이상D,그외F 
def result(temp):
    if temp>=90:
        result='A'
    elif temp>=80:
        result='B'
    elif temp>=70:
        result='C'
    elif temp>=60:
        result='D'
    else:
        result='F'
    return result

df1=pd.read_excel('stu1000.xlsx')

df1['합계']=df1['국어']+df1['영어']+df1['수학']+df1['과학']+df1['사회']
df1['평균']=df1['합계']/5
df1['평가']='F'
df1['평가']=df1['평균'].apply(result)
print(df1)



# [ 문제 3 ] 합계점수가 400점이상인 학생의 수학평균을 구하시오.
filt=df1['합계']>=400
print(df1.loc[filt,'수학'].mean())



# [ 문제 4 ] 자료실 train.csv 파일을 다운
df2=pd.read_csv('train.csv',index_col='PassengerId')

# print(df2.columns)

# 1) 남자(male)이면서 pclass가 1인 승객을 출력하시오.
print(df2[(df2['Sex']=='male')&(df2['Pclass']==1)])

# 2) Survivied 1이면서 age 20이하인 승객을 출력하시오.
print(df2[(df2['Survived']==1)&(df2['Age']<=20)])

# 3) 그룹 survivied,pclass 컬럼으로 수를 출력하시오.
print(df2.groupby(['Survived','Pclass']).count())



# [ 문제 5 ] 2개의 2차원데이터가 있습니다. 
data1={
    '이름':['주바다','공유진','송선유','양홍욱'],
    '성별':['여','여','여','남'],
    '전화번호':['010-1111-1111','010-1111-2222','010-1111-3333','010-1111-4444']
}
data2={
    '이름':['공유진','주바다','윤상운','송선유'],
    '국어':[100,99,95,100],
    '영어':[95,99,99,100]
}

member=pd.DataFrame(data1)
score=pd.DataFrame(data2)

# 1) 2차원데이터를 DataFrame 형태로 만들어서, 2개의 데이터를 같은 것만 존재하도록 join하시오. 
mdf=pd.merge(left=member,right=score,how='inner',on='이름')
print(mdf)

# 2) 2개의 데이터 모두 존재하도록 join하시오.
mdf2=pd.merge(left=member,right=score,how='outer',on='이름')
print(mdf2)
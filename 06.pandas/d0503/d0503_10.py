# stu1000.xlsx 파일 읽어와서
# 1.합계, 평균 컬럼을 추가하고, 
# 2.학교,학년컬럼 그룹으로 합계를 역순정렬
# 3.학교,학년컬럼 그룹으로 각 학교, 학년별 평균을 구하고 합계컬럼 기준으로 역순정렬
 
import pandas as pd

def school(temp):
    if temp==1:
        result='구로고'
    elif temp==2:
        result='디지털고'
    else:
        result='단지고'
    return result

df=pd.read_excel('stu1000.xlsx',index_col='학번')
df['학교']=df['학교'].apply(school)

df['합계']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['평균']=(df['합계']/5).astype(int) # df['합계']//5 사용가능

print(df.groupby(['학교','학년']).sum().sort_values('합계',ascending=False))
print(df.groupby(['학교','학년']).mean().sort_values('합계',ascending=False))
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=10
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np
import re

def strchange(temp):
    result=float(re.sub(r'[^0-9.]','',temp))
    return result

df=pd.read_csv('chipotle.tsv',sep='\t')
# 타입변경
df['order_id']=df['order_id'].astype(str)
df['item_price']=df['item_price'].apply(strchange) # $표시 없애주기

# 1. 가장 주문을 많이 한 상품 5개
find_df=df.groupby('item_name')['order_id'].count().sort_values(ascending=False).head(5)
print('<가장 주문을 많이 한 상품 5개>')
print(find_df)
print('-'*50)

# 2. 총주문수를 출력하시오.
# 1) 주문한 메뉴(item_name)의 종류를 출력하시오.
# 2) 주문한 메뉴(item_name) 종류의 수를 출력하시오.
print('<주문한 메뉴 종류>')
item_names=df['item_name'].sort_values().unique()
print(item_names)
num=df['item_name'].nunique()
print('주문한 메뉴 종류의 수 : ',num)
print('-'*50)


# 3. item_name당 주문개수(order_id)와 총량(합계, quantity)을 출력하시오.
print('<item_name quantity 몇개인지 출력>')
print(df.groupby('item_name')['quantity'].sum())
print('-'*50)
print('<item_name order_id 몇개인지 출력>')
print(df.groupby('item_name')['order_id'].count())
print('-'*50)

# # item_name당 총 판매액
# print(df.groupby('item_name')['item_price'].sum())

# 4. order_id 주문당 평균 계산금액을 출력
print('<order_id 주문당 평균 계산금액을 출력>')
print(df.groupby('order_id')['item_price'].mean())
print('평균주문금액 : {:.2f} 달러'.format(df.groupby('order_id')['item_price'].sum().mean()))
print('-'*50)


# 5. 막대그래프로 표현하시오.
# title:주문량그래프
# ylabel: 주문량, xlabel: 주문번호
fig_df=df.groupby('item_name')['order_id'].count()
print(fig_df)

x=np.arange(num)
plt.figure(figsize=(10,8))
plt.title('주문량 그래프')
plt.bar(x,fig_df)
for i,txt in enumerate(fig_df):
    plt.text(i,txt+2,txt,ha='center')

plt.xticks(x,item_names,rotation=90)
plt.show()
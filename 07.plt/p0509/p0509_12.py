import enum
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=10
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df=pd.read_csv('chipotle.tsv',sep='\t')
# # chiplotle 데이터 구조 파악필요
# print(df.columns)
# ['order_id', 'quantity', 'item_name', 'choice_description','item_price']

# print(df.info())
# print(df.shape) # index:4622, column:5
print(df.groupby('item_name').mean())

# 타입변경
df['order_id']=df['order_id'].astype(str)

# 중복제거 후 order_id
print(df['order_id'].unique())
print(df['order_id'].nunique())

# 주문한 메뉴 개수 : 50
print(df['item_name'].nunique())

# ### 1. 가장 많이 주문한 item_name, value_counts() 하면 딤
# 자동으로 역순절렬이 되어서 출력이됨
# 가장 많이 주문한 item_name
# item_count=df['item_name'].value_counts()
item_count=df['item_name'].value_counts()[:10] #10등까지 보여줄수 있음
print(item_count)
print(item_count.shape)

# iteritems 2개의 열을 가져올 수 있음
for i, (val,cnt) in enumerate(item_count.iteritems()):
    # val=item_name
    # cnt=quantity
    print('주문 : ',val,cnt)
    
#### item_name당 주문한 개수
order_count = df.groupby('item_name')['order_id'].count()
print(order_count)

#### item_name당 주문량 - quantity int 타입, 수량을 더해서 가져와야햠
item_quantity = df.groupby('item_name')['quantity'].sum()
print(item_quantity)

#### order_id 주문당 평균 계산금액을 출력
# lambda : 간편함수 정의 --> x에 대한 식을 정의해주는데 1부터 잘라서 float으로 형변환해줌
# def fun():
#     x=float(x[1:])
#     return x
df['item_price']=df['item_price'].apply(lambda x:float(x[1:]))
# df['item_price']=df['item_price'].apply(fun)
print('평균주문금액 : {:.2f} 달러'.format(df.groupby('order_id')['item_price'].sum().mean()))


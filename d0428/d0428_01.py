# Series : pandas 1차원 데이터

import pandas as pd

# # 1차원 데이터 생성
# temp=pd.Series([-20,-10,10,20])
# print(temp)

# # 0번째 주소 출력
# print(temp[0])

# print(temp[3])

arr=[1,2,3,4,5,6,7]
# 여러개의 데이터가 있을 때 위치를 쉽게 찾을 수 있음
temp=pd.Series(arr)

print(temp)




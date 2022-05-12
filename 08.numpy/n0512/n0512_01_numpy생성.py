import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# list
list_data=[1,2,3]
print(list_data)
# list 0번째 주소 출력
print(list_data[0])

# for i in range(len(list_data)):
#     list_data[i]=list_data[i]+3
# print(list_data) # list에는 더할수 없음
# list타입에 3 더하기 불가능
# print(list_data+3) # list에는 더할수 없음

# numpy형태로 변경
arr=np.array(list_data)
print(arr)
print(arr[0])
# 모든 행렬에 3을 더함
print(arr+3)

# numpy 배열 크기
print(arr.shape) 
# numpy 배열 크기
print(arr.size)
# numpy 타입
print(arr.dtype)
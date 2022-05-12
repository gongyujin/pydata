import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd

list_data=[
    [1,2,3],
    [4,5,6]
]
print(list_data)

# 2차원 배열 numpy생성
arr=np.array(list_data)
print(arr.shape) # 2행 3열의 행렬
print(arr[0,1])

# arange 사용 : 순차적인 numpy행렬을 생성 --> 0,4 이전까지 생성
arr1=np.arange(4)
print(arr1)

# 2부터 9까지 행렬 생성 : (시작 2, 끝 10이전)
arr2=np.arange(2,10)
print(arr2)

# 1,3,5,7,9 행렬 생성 : (시작 1, 끝 10이전, 2씩 증가)
arr3=np.arange(1,10,2)
print(arr3)

arr4=np.arange(0,10,3)
print(arr4)

# # list를 직접생성하지 않고, numpy행렬을 사용하면 쉽게 list를 만들수 있음
# x1=np.arange(1,11)
# print(x1)

# # x=[1,2,3]
# y=[2,4,8,10,8,6,4,2,4,6]

# # matplotlib 그래프 데이터 사용가능
# plt.plot(x1,y)
# plt.show()
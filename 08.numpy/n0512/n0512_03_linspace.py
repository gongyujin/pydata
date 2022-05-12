import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd

# 행렬 4개 생성
arr1=np.arange(1,11)
print(arr1)

# linspace : 1부터 10까지 균등하게 4개의 행렬생성
arr2=np.linspace(1,10,4) 
arr2=np.linspace(0,10,5,retstep=True) # 사이간격값: retstep=True
print(arr2)

# 개수가 없으면 디폴트 50개 생성
arr3=np.linspace(0,10)
print(arr3)



# list_data=[0,1,2,3,4]
# print(list_data)
# # numpy 타입변경 : dtype=float
# # arr=np.array(list_data,dtype=float)
# arr=np.array(list_data)
# print(arr)
# arr=np.array(list_data,dtype=str)
# print(arr.dtype)
# print(arr)

# arr2=np.arange(5)
# print(arr2)

# arr3=np.arange(0,5)
# print(arr3)

# arr4=np.arange(0,21,5)
# print(arr4)
from matplotlib.pyplot import axes
import numpy as np

# # 1차원 행렬 concatenate 결합 : 옆으로 결합
# arr=np.arange(10)
# arr2=np.arange(10,20)
# arr3=np.concatenate([arr,arr2],axis=0)
# print(arr3)

# # 2차원 행렬 concatenate 결합 : axis=0기준
# 행기준으로 합칠때 행의 개수가 맞아야 가능
# arr1=np.arange(4).reshape(1,4) # 2차원행렬
# print(arr1)
# print(arr1.shape)
# arr2=np.arange(8).reshape(2,4) # 2차원행렬
# print(arr2)
# print(arr2.shape)

# # 2차월배열 합치기, 디폴트: axis=0 (행이 기준)
# arr3=np.concatenate([arr1,arr2],axis=0)
# print(arr3)
# print(arr3.shape)

# concatenate axis=1기준 : 열기준으로 행렬 합치기
# 열기준으로 합칠때는 열의 개수가 맞아야 가능
arr1=np.arange(4).reshape(2,2)
arr2=np.arange(4,8).reshape(2,2)
arr3=np.concatenate([arr1,arr2],axis=1)
print(arr3)
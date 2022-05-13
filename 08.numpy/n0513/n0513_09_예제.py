import numpy as np

# 1. [[1,1],[0,1]] (2,2)행렬, [[2,0],[3,4]] 행렬,
# 두행렬의 곱셈의 결과와 단위행렬 곱을 구하시오.
arr1=[[1,1],[0,1]]
arr2=[[2,0],[3,4]]
result_arr1=np.multiply(arr1,arr2)
print(result_arr1)
result_arr2=np.dot(arr1,arr2)
print(result_arr2)
print('-'*30)
# 2. 1부터 6까지 (2,3)행렬 + 7부터 12까지 (3,2)행렬
# 행렬의 단위행렬 곱을 구하시오.
arr3=np.arange(1,7).reshape(2,3)
arr4=np.arange(7,13).reshape(3,2)
result_arr3=np.dot(arr3,arr4)
print(result_arr3)
print('-'*30)

# 3. 1부터 9까지 (3,3)행렬을 만들고,
# 1행줄에 곱하기 2, 2행줄에 곱하기 3을 해서 출력하시오.
arr5=np.arange(1,10).reshape(3,3)
print(arr5)
arr5[1]=arr5[1]*2 # 1행전체*2
arr5[2]=arr5[2]*3 # 2행전체*3
print(arr5)
print('-'*30)



# arr=np.arange(3)
# arr2=np.arange(3)
# arr3=np.dot(arr,arr2)
# print(arr.shape) # 1x5행렬이 아니라 1차원배열이기 때문에 5라고 생각해야함
# print(arr3) # 1차원끼리의 단위행렬을 할때는 리스트의 길이를 맞춰야함
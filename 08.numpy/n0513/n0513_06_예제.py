import numpy as np

# 1. 1로 채워진 (2,3)행렬을 생성하시오.
arr1=np.ones((2,3))
# arr1=np.full((2,3),1)
# arr=np.arange(6).reshape(2,3)
# arr=np.where(arr<7,1,1)
print(arr1)
# 2. rand 랜덤으로 (2,3)행렬을 생성하시오.
arr2=np.random.rand(2,3)
print(arr2)
# 1번 행렬에 3을 곱해 출력하시오.
arr3=arr1*3
print(arr3)
# 1번 행렬에 2번 행렬을 더해서 출력하시오.
arr4=arr1+arr2
print(arr4)
import numpy as np

# 1. 1부터 100사이의 랜덤수를 넣어서, (10,10)행렬을 생성하시오.
# -위 행렬에서 50이상인 값을 출력하시오.
arr1=np.random.randint(1,101,(10,10))
print(arr1)
idx=np.where(arr1>=50)
print(arr1[idx])
print(arr1[idx].size)

# 2. 0부터 20사이 랜덤수를 넣어서, 10보다 크면 그대로, 10보다 작으면 0을 입력하시오.
arr2=np.random.randint(0,21,20)
print(arr2)
arr3=np.where(arr2>10,arr2,0)
print(arr3)
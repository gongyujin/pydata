import numpy as np

# 1. 0-7까지 1차원 행렬, (2,4) 2차원 행렬로 변경하고,
# 다시 (2,2)의 3차원 행렬로 변경하시오.
arr1=np.arange(0,8).reshape(2,4) #2*4=8개
arr1_1=arr1.reshape(-1,2,2) #2*2*2=8개
print(arr1_1)
# 3차원 배열에서 숫자 4를 출력하시오.
print(arr1_1[1][0,0])
# print(arr1_1[1,0,0])
# 3차원 배열에서 숫자 3를 출력하시오.
print(arr1_1[0][1,1])
print(arr1_1[1,1,0]) # 6출력

# 2. 1부터 4까지 (2,2) 행렬로 생성하고, 2값을 출력하시오.
# - 2차원행렬을 1차원 행렬로 변경하시오.
arr2=np.arange(1,5).reshape(2,2)
print(arr2[0][1]) # 2
print(arr2.reshape(4))
# flatten(): 1차원 행렬 변경
print(arr2.flatten())

# 3. 15,8,12,11,7,3 (2,3)행렬을 만드시오.
# - 10보다 큰수가 몇개인지 출력하시오.
arr3=np.array([15,8,12,11,7,3]).reshape(2,3)
idx=np.where(arr3>10)
print(arr3[idx].size)
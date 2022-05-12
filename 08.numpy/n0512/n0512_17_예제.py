import numpy as np

# (3,5)행렬 : 1로 채우기
# (3,2)행렬 : 랜덤 1,10 숫자를 채우기
arr1=np.ones([3,5])
arr2=np.random.randint(1,10,(3,2))
print(arr1)
print(arr2)

# 열기준으로 행렬 합치기
arr3=np.concatenate([arr1,arr2],axis=1)
print(arr3)

# 열기준으로 (3,4)(3,3) 형태로 나누기
left,right=np.split(arr3,[4],axis=1)
print(left)
print(right)

# 행기준으로 (2,7)(1,7) 행렬 나누기
top,bottom=np.split(arr3,[2],axis=0)
print(top)
print(bottom)

import numpy as np

# 1. 행렬조건
# 랜덤(randn)으로 (4,4)행렬을 만들고,
# 0보다 큰행렬은 2, 작은행렬은 -2로 변경하시오.
arr1=np.random.randn(4,4)
arr2=np.where(arr1>0,2,-2)
print(arr2)

# 2. 행렬2개를 만들어서 합치기
# 1부터 11까지 홀수 (3,2) 행렬 생성,
# 2부터 12까지 짝수 (3,2) 행렬 생성후 행으로 결합하시오.
arr3=np.arange(1,12,2).reshape(3,2)
arr4=np.arange(2,13,2).reshape(3,2)

arr5=np.concatenate([arr3,arr4],axis=0)
print(arr5)
arr6=np.concatenate([arr3,arr4],axis=1)
print(arr6)

# 3. 행렬분리
# 0부터 99까지 (10,10) 행렬을 만든 후,
# 3열을 기준 2개의 행렬로 분리하시오.
arr7=np.arange(100).reshape(10,10)
# 열기준으로 짜르기
left,right=np.split(arr7,[3],axis=1)
print(left)
print(right)
# 행기준으로 짜르기
top,bottom=np.split(arr7,[5],axis=0)
print(top)
print(bottom)
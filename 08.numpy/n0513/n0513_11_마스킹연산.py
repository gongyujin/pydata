import numpy as np

# 1. 1부터 100까지 랜덤수를 50개를 만들고, (5,10)행렬을 변경후
# 짝수만 찾아서 출력하시오.
arr1=np.random.randint(1,101,(5,10))
idx=arr1%2==0
print(arr1)
print(arr1[idx])

# 짝수 *10, 홀수 *2로 변경한 행렬을 출력하시오.
idx_arr=np.where(arr1%2==0,arr1*10,arr1*2)
print(idx_arr)

# 50보다 작은 수는 모두 100으로 변경하시오.
idx_arr2=np.where(arr1<50,100,arr1)
print(idx_arr2)
# 조건의 결과가 1개만 있으면 마스킹연산
idx2=arr1<50
arr1[idx2]=100
print(arr1)

# list1=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# arr=np.array(list1)

# idx_arr=[
#     [False,True,False],
#     [True,True,False],
#     [False,False,True]
# ]
# idx=np.array(idx_arr)
# # 마스킹 연산
# print(arr[idx])

# arr=np.random.randint(1,10,(5,5))
# print(arr)

# # where절을 사용하여 행렬 크기 존재
# idx_arr=np.where(arr>5,arr,0)
# print(idx_arr)

# # 마스킹 연산
# idx_arr=arr>5
# print(idx_arr)
# print(arr[idx_arr])

# # 2차원 행렬
# arr=np.arange(9).reshape(3,3)
# print(arr)
# # boolean indexing
# bol_arr=arr>5
# print(bol_arr)
# print(arr[bol_arr]) # 해당되는 것만 1차원 배열형태로 출력
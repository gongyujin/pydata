import numpy as np

list_data=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

arr=np.array(list_data)
# list_data2=np.arange(1,13).reshape(3,4)
print(arr)

# list1=[1,2,3,4,5,6]
# print(list1[2])
# # numpy 인덱싱 - 1개 인덱싱
# print(arr[0,1])
# print(arr[0,2]) # 3의 데이터

# # numpy indexing - 2개이상 가져올때 
# idx=arr[[0,2],[1,3]] # [[0,2],[1,3]] => (0,1),(2,3)
# print(idx)

idx=arr[[0,1,2],[1,2,3]]
print(idx)


# # 1부터 50으로 (5,10)행렬을 출력하시오.
# arr1=np.arange(1,51).reshape(5,10)
# print(arr1)
# # 슬라이싱
# # 행 3부터 4까지, 열은 5부터 9까지 출력하시오.
# # arr2=arr1[3:5,5:10]
# arr2=arr1[3:,5:]
# print(arr2)

# # 1차원행렬
# arr3=np.arange(50)
# print(arr3)
# # 1차원 행렬 슬라이싱
# print(arr3[3:10])


# # 슬라이싱
# lst=[[1,2,3],
#      [4,5,6],
#      [7,8,9]
#      ]

# arr=np.array(lst)

# # 슬라이싱 앞부분 0:2 -행 0부터 2앞까지 1, 0~1까지 행을 가져옴
# arr2=arr[0:2] 
# # 0:2 0부터1까지 행, 0:2 0부터 1까지 열
# arr2=arr[0:2,0:2]
# arr2=arr[0:2,1:2] #0부터1까지, 1까지

# # 1부터 끝까지, 1부터 끝까지
# arr2=arr[1:,1:]

# # 0부터 끝까지 행, 0부터 1까지 열
# arr2=arr[0:,0:2]


# print(arr2)
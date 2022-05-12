import numpy as np

#### 1차원 행렬 where
# # where
# arr=np.arange(10) # 1차원행렬
# arr2=arr.reshape(2,-1) #(2,5)
# print(arr2)

# # 4*5=20
# arr3=np.arange(20).reshape(4,5)
# print(arr3)

# arr=np.arange(4,15) # 1차원행렬
# print(arr)
# idx=np.where(arr%2==0)
# print(np.where(arr%2==0)) # 위치를 출력해줌
# # 배열에 넣으면 index 해당값만 출력시켜줌
# print(arr[idx])

# arr=np.random.randint(1,10,20)
# # 짝수인것만 출력
# print(arr[np.where(arr%2==0)])

# arr2=np.arange(1,21)
# # where 조건식에 맞는 형태의 행렬주소를 알려줌
# idx=np.where(arr2>10)
# # 행렬에 넣으면 해당핼렬만 출력
# print(arr2[idx])


# # 2차원 행렬 where
# arr=np.arange(10).reshape(2,-1)
# print(arr)
# idx=np.where(arr%2==0)  
# print(idx) # indexing을 하게 되면 x, y 개념으로 합쳐서 위치 찾아야함
# print(arr[idx]) # 행렬 한개짜리로 넘어옴

# arr=np.arange(20).reshape(4,5)
# idx=np.where(arr%2==0)
# print(arr[idx])

# # where 행렬에서 3보다 큰수를 출력
# arr=np.array([2,5,1,3,0,6,5,4,7,2,9])
# idx=np.where(arr>3)
# print(arr[idx])

arr=np.arange(20)
# where 3의 배수이면 그대로 출력, 3의 배수가 아니면 0으로 출력
# where (조건식,True일때, False일때)
# idx=np.where(arr%3==0,arr,0)
idx=np.where(arr<10,arr,1)
print(arr[idx])


### 3차원 행렬
arr3=np.arange(20)
# 2*5*2=20
arr4=arr3.reshape(2,5,2) # 2개 *(5행2열)
# arr4=arr3.reshape(2,5,-1) # z,x,y
print(arr4)

# 2차원 행렬
a1=np.arange(10).reshape(5,2)
print(a1)
a2=np.arange(10,20).reshape(5,2)
print(a2)

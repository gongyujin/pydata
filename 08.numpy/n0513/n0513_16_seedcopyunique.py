import numpy as np

# 중복제거 후 출력
list1=[1,3,4,3,1,5,7,7,9]
arr=np.array(list1)
print(arr)
# 행렬에 중복이 있을 경우 중복을 제거하고 출력
print(np.unique(arr))
print(len(np.unique(arr)))


# # 깊은 복사
# # 값저장 주소를 다르게 하려면 copy
# arr=np.arange(10)
# arr2=arr.copy()
# arr2[0]=1000
# print(arr2)
# print(arr)

# # 행렬의 위치값을 입력하면 그값이 변경
# arr=np.arange(10)
# print(arr)
# arr[3]=100
# print(arr)

# # 행렬 복사 -> 얕은 복사
# arr2=arr
# print(arr2)

# arr2[0]=1000
# print(arr2)
# print(arr) # 주소값이 같기때문에 arr2를 변경하면 arr도 같이 변경됨

# # 랜덤숫자를 1번만 생성후 랜덤숫자가 변경되지 않음
# np.random.seed(7)
# arr=np.random.randint(0,10,(2,3))
# print(arr)

# arr=np.random.randint(0,10,(2,3))
# print(arr)

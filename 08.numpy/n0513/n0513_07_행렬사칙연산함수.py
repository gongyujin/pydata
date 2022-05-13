import numpy as np

arr1=np.arange(4).reshape(2,2)
arr2=np.arange(2).reshape(1,2)


# # 두수의 더하기
# idx1=np.add(10,100)
# print(type(idx1))

# idx2=np.subtract(10,100)
# print(idx2)

# idx3=(10-100)
# print(type(idx3))

# print(arr1-arr2)
# print(np.subtract(arr1,arr2))

# 곱하기 함수
idx3=np.multiply(arr1,arr2)
print(idx3)

# 나누기 함수
idx4=np.divide(arr1,arr2)
print(idx4)

# 제곱
idx5=np.power(2,5)
print(idx5)

# 제곱근
idx6=np.sqrt(2)
print(idx6)




### numpy 행렬 구주가 다른 경우 더하기 : broadcast됨, 행태를 맞춰줌
# # 반드시 열의 구조는 맞아야 연산을 할 수 있음
# # (2,2)행렬
# arr1=np.arange(6).reshape(2,3)
# # arr1=np.arange(8).reshape(2,4) # 행렬의 구조가 맞지 않아 error
# print(arr1)
# # (2,)행렬
# arr2=np.arange(3)
# print(arr2)

# arr3=arr1+arr2
# print(arr3)




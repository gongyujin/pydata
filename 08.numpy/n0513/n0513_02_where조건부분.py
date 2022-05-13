import numpy as np

# where
arr=np.arange(8)
# where절에 조건식만 존재 ==> 조건식에 True,False가 들어가있음, idx나옴 (위치값이 존재)
# 0 1 2 3 4 5 6 7 : 0 1 2 3 4 5는 False, 6 7은 True
idx1=np.where(arr>5)
print(arr[idx1])

# # 조건식만 넣으려면 where절을 사용할 필요가 없음
# idx=arr>5
# print(idx)
# print(arr[idx])


# where절에 조건과 결과식이 포함 : 온전한 배열으로 나옴
idx2=np.where(arr>5,100,0)
print(idx2)


# 1~8까지 2,2배열
arr=np.arange(1,9).reshape(2,-1)
print(arr)
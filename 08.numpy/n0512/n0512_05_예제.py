import numpy as np

# 1. 3부터 9까지 1차원 배열 생성후,  첫번째 요소를 출력하시오
arr1=np.arange(3,10)
print(arr1[0])

# 2. 배열 [5,5]를 생성하고 1로 값을 채우시오
arr2=np.full((5,5),1)
print(arr2)

# 3. 4 2 1 5 2 6 1 1 1 을 (3,3) 배열로 출력하시오.
# -list를 만든후, 3,3배열을 출력
arr3=[
    [4,2,1],
    [5,2,6],
    [1,1,1]
    ]
arr3=np.array(arr3)
print(arr3)
list_data=[4,2,1,5,2,6,1,1,1]
rearr3=np.array(list_data).reshape((3,3))
print(rearr3)

# 4. 0부터 30까지 2씩 배열을 출력하시오.
arr4=np.arange(0,31,2)
print(arr4)

# 5. 0에서 4까지 9개의 수를 균일한 간격으로 출력하시오.
# arr5=np.linspace(0,4,9,retstep=True) # type : 튜플
arr5=np.linspace(0,4,9) # type : numpy.ndarray, float
print(type(arr5))
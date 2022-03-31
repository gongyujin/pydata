# temp =[
#     [1, 2, 3, 4, 5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]
from random import *

# randNum=[i+1 for i in range(25)]
# 1. 랜덤리스트 생성
randNum=[]
# 2. 랜덤리스트에 1-25까지 입력
for i in range(25):
    randNum.append(i+1)

# 3. 랜덤 섞기
for i in range(500):
    rno=randint(0,24)
    randNum[0],randNum[rno]=randNum[rno],randNum[0]

arrs=[]
# randNum 에 있는 데이터를 arrs에 list를 만들어 추가
for i in range(0,5):
    # i= 0,1,2,3,4           j=0,1,2,3,4
    arr2=[randNum[5*i+j] for j in range(0,5)]
    arrs.append(arr2)
 
# print(arrs)   

# 무한반복    
while True:
    # 출력
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end=' ')
        print() 
    
    # 원하는 숫자 입력
    input1=int(input('1-25의 숫자를 입력하세요.>> '))
    # 3이라는 숫자를 넣으면 3의 자리에 x가 입력되도록 구현 
    for i, arr in enumerate(arrs):
        if input1 in arr:
            # [1,2,3,4,5] 3의 위치 arr.index(3) -> 2라고 반환 됨
            arrs[i][arr.index(input1)]= 'X'    
#---------------------------------------------------------------
 
# arr1=[]

# # 2차원 list에 1-25까지의 숫자 입력
# for i in range(0,5): #0,1,2,3,4
#     # 5*i:0,1,2,3,4    j:1,2,3,4,5
#     arr2=[5*i+j for j in range(1,6)]
#     arr1.append(arr2)

# # 무한반복    
# while True:
#     # 출력
#     for arr in arr1:
#         for a in arr:
#             print('{:2s}'.format(str(a)),end=' ')
#         print() 
    
#     # 원하는 숫자 입력
#     input1=int(input('1-25의 숫자를 입력하세요.>> '))
#     # 3이라는 숫자를 넣으면 3의 자리에 x가 입력되도록 구현 
#     for i, arr in enumerate(arr1):
#         if input1 in arr:
#             # [1,2,3,4,5] 3의 위치 arr.index(3) -> 2라고 반환 됨
#             arr1[i][arr.index(input1)]= 'X'        
    
    
# # # 0으로 채워진 5*5 2차원 배열을 생성하시오.
# # zero1=[]

# # for i in range(5):
# #     zero2=[0 for j in range(5)]
# #     zero1.append(zero2)
    
# # print(zero1)


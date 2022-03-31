# import random
from random import *
numList=[i for i in range(1,46)]
print(numList)
shuffle(numList) # 리스트 섞기가 가능한 함수, 파괴함수: 원본데이터가 손상됨(수정됨), 원본데이터를 복구할 수 없음
print(numList)
print(sample(numList,5 )) # 리스트 중 해당되는 수만큼 선택가능한 함수



# # 소수점 3자리에서 반올림해서 출력하시오.
# a=random.random()
# print(a)
# print(round(a,2))
# print(round(a*100)/100)



# print(random.random()) #shift+alt+방향키
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())

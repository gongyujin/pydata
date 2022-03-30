# 리스트 1, 45까지의 숫자를 넣어보세요.
# numbers=[]
# for i in range(1, 46):
#     numbers.append(i)
from random import *

#lotto 번호 부여 1-45
numbers = [i for i in range(1,46)] 
#lotto 번호 섞음   
for i in range(500):
    #랜덤숫자
    rannum=randint(0,44)
    #두수 교환
    numbers[0], numbers[rannum]= numbers[rannum], numbers[0]

# temp = numbers[0]
# numbers[0] = numbers[rannum]
# numbers[ran_num] =temp




print(numbers)
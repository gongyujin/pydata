import random
from random import *

# #lotto 6개를 저장해서 출력하시오.
# #list에 저장을 해보세요.
lotto=[] #로또번호 저장리스트
# # 6번 반복
# # random 숫자 중복되지 않게 6 숫자 저장
# for i in range(0,6):
#     temp=randrange(1,46) #랜덤숫자 발생

#     if temp not in lotto: #lotto에 temp 중복숫자가 없을경우에만 저장
#         lotto.append(temp)

        
# print(lotto)


count=0
while True: #무한반복
    if count<=5: #5보다 작거나 같을때 실행
        temp=randrange(1,46) #랜덤숫자 발생
        # 랜덤숫자가 lotto리스트에 있는지 비교
        if temp not in lotto: #lotto에 temp 중복숫자가 없을경우에만 저장
            lotto.append(temp)
            count+=1
    else:
        print('6개의 번호가 추출되었습니다.')
        break
    
print(lotto)
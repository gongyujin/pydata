# lotto 리스트에 6개의 랜덤숫자를 넣으시오.
# 중복 제거
# 숫자 6개를 입력받으시오. : 몇개를 맞추는지 맞추기

import random
from random import * # 불러왔기 때문에 random.randrange라고 안써도 됨

# 1. 변수선언
lotto=[] #로또번호
count=0
my_count=0
co_num=[] #맞춘 번호

# 2. 입력숫자 6개 
my_num=[] #입력번호
for i in range(6):
    a=int(input('{}번째 숫자를 입력하세요.>> '.format(i+1)))
    my_num.append(a)

# 3. 랜덤숫자 6개 받기
while True:
    if count <=5:
        
        temp=randrange(1,46)
        
        if temp not in lotto:
            lotto.append(temp)
            count+=1
    else:
        print('로또 6개가 입력되었습니다')
        break
    

# 4. 로또번호와 입력번호가 몇개 맞는지 출력하시오.
for i in range(6):
    
    if my_num[i] in lotto:
        my_count+=1
        co_num.append(my_num[i])

# 5. 출력   
print('로또 번호: ', lotto)  
print('내가 입력한 로또 번호: ', my_num)
print('로또 맞춘 개수: ', my_count)
print('내가 맞춘 로또 번호: ', co_num)
# import random # random.randint() 라고 써야하지만 *로 다 불러왔기 때문에 randint()만써도 됨
from random import *

# 1. 리스트 생성
# 2. 리스트 1-25까지 숫자입력
randNum=[i+1 for i in range(25)]

# print(randNum)

# 3. 랜덤섞기
for i in range(200):
    rno=randint(0,24)
    randNum[0],randNum[rno]=randNum[rno],randNum[0]

# print(randNum)

# 4. 2차원배열 리스트 생성
arrs=[]

# 5. 1차원 리스트를 2차원 리스트에 추가
for i in range(0,5):
    # arr2=[5*i+j for j in range(1,6)] # 숫자를 순차적으로 넣음
    arr2=[randNum[5*i+j] for j in range(0,5)] # 랜덤숫자를 넣음
    arrs.append(arr2)
# print(arrs)


# 6. 2차원리스트 출력
# 7. 무한루프 
while True:
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end=' ')
        print()
    
    print('-'*40)
    
    # 원하는 숫자를 입력받음
    input1=int(input('원하는 번호를 입력하세요. (0: 프로그램 종료)>> '))

    
    if input1==0:
        print('프로그램 종료')
        break
    
    # 8. 입력된 숫자를 x표시로 변경
    for i,arr in enumerate(arrs): 
        if input1 in arr:
            arrs[i][arr.index(input1)] = 'X'
            
    
from random import *
# 1. 랜덤리스트 생성
randNum=[]
# 2. 랜덤리스트에 1-25 입력
for i in range(25):
    randNum.append(i)
    
# 3. 랜덤 섞기
for i in range(500):
    rno=randint(0,24)
    randNum[0],randNum[rno]=randNum[rno],randNum[0]
    
# 4. 2차원 리스트 만들기
arrs=[]
for i in range(5):
    arr2=[randNum[5*i+j] for j in range(0,5)]
    arrs.append(arr2)
    
# 5. 무한반복
while True:
    # 5-1 출력
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end=' ')
        print()
    # 5-2 x입력 구현        
    input1=int(input('1-25사이 숫자를 입력하세요.>> '))
    for i, arr in enumerate(arrs):
        if input1 in arr:
            arrs[i][arr.index(input1)] = 'X'
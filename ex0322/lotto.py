from random import *

# 로또번호 입력함수
def inputNo(lottoInput):
    for i in range(6):
        no=int(input('로또 번호를 입력하세요.>> '))
        lottoInput.append(no)

# 로또번호 생성함수
def lottoProduce(lottoNum): # 지역변수에서 주소가 복사되었기 때문에 값이 바뀌면서 원래 값의 데이터가 변경된 상태로 저장됨
    for i in range(45):
        lottoNum.append(i+1) # 함수를 빠져나오면서 지역변수는 삭제됨
 
# 로또번호 섞기함수
def lottosuffle(lottoNum, lotto6):
    for i in range(500):
        temp=randint(0,44)
        lottoNum[0],lottoNum[temp]=lottoNum[temp],lottoNum[0]
    
    for i in range(6):
        lotto6.append(lottoNum[i])
        
def lottoOk(okNum, lotto6, lottoInput,count):
    for i in range(6):
        if lottoInput[i] in lotto6:
            okNum.append(lottoInput[i])
            count+=1
    return count
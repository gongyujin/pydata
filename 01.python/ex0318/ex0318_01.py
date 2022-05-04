from random import *

# 자신이 입력한 6개의 숫자와 로또 당첨번호 6개와 비교해서
# 몇개를 맞췄는지 출력하는 프로그램을 구현하시오.

#당첨번호: 32, 1, 42,17, 3919
#입력번호: 1,2,3,4,5,6
#당첨개수: ㅁ개
#당첨금액: ㅁ백만원

reward=['꽝!','1천만원','5백만원','5천만원','1억원','50억원','100억원']
# 6개 : 100억
# 5개 : 50억
# 4개 : 1억
# 3개 : 5천만원
# 2개 : 5백만원
# 0개: 꽝!

# <옵션>
# 자신이 입력한 번호가 보여지면서 입력을 받음.
# 1-45까지의 번호가 있고, 입력한 번호는 x가 표시가 되게 화면구현

mylotto=[] #내가 입력한 로또 번호 리스트
lotto=[] # 당첨번호 리스트
count=0
mycount=0
okNum=[] # 당첨된 번호 리스트

lotto_num=[i+1 for i in range(45)] 
mark_lotto=[i+1 for i in range(45)] # 45개 번호 생성 리스트

#-------------------------------------------------------   
# 당첨 번호 만들기    
# # 로또 번호 6개 생성하기
# while True:
#     if count < 6:
#         rno=randint(0,44)
#         if not rno in lotto:
#             lotto.append(rno)
#             count+=1
#     else:
#         print('번호 6개가 입력되었습니다.')
#         print('-'*30)
#         break
# lotto=sample(mark_lotto,6)

for i in range(500):
    rno=randint(0,44)
    lotto_num[0],lotto_num[rno]=lotto_num[rno],lotto_num[0]

lotto=lotto_num[0:6]

#-------------------------------------------------------   
# 당첨된 번호를 x표시로 만들기 (빙고판 45개중에 내가 입력한 번호만 지우기)
# 2차원 리스트 만들기
print('[ LOTTO CARD ]')
print('-'*30)
for i in range(5):
        for j in range(10):
            if count < 45:
                print('{:2s}'.format(str(mark_lotto[10*i+j])),end=' ')
                count+=1
            else:
                break
            
        print()



# temp count 추가
# while 문
for idx in range(6):
    
    a=int(input('{}번째 로또 번호를 입력하세요.>> '.format(idx+1)))
    print()
    mylotto.append(a)
    mark_lotto[a-1]='X'
    
    
    count=0 #45까지 출력되도록 체크하는 변수
    print('[ LOTTO CARD ]')
    print('-'*30)
    for i in range(5):
        for j in range(10):
            if count < 45:
                print('{:2s}'.format(str(mark_lotto[10*i+j])),end=' ')
                count+=1
            else:
                break
            
        print()
    print('-'*30)
    
    
    

# arrs=[]
# for i in range(0,5):
#     arr2=[mark_lotto[9*i+j] for j in range(0,9)]
#     arrs.append(arr2)
    
# # 9*5 형태로 보여주기
# ct=0
# while True:
#     for arr in arrs:
#         for a in arr:
#             print('{:2s}'.format(str(a)),end=' ')
#         print()
#     print()
    
#     # 내 로또 번호 입력하기
    
#     if ct < 6:
#         ct+=1
#         a=int(input('{}번째 로또 번호를 입력하세요.>> '.format(ct)))
#         mylotto.append(a)
#         for i,arr in enumerate(arrs):
#             if a in arr:
#                 arrs[i][arr.index(a)] ='X'     
#     else:
#         break
    
#     print('-'*30)


# # 내 로또 번호 입력하기
# for i in range(6):
#     a=int(input('{}번째 숫자를 입력하세요.>> '.format(i+1)))
#     mylotto.append(a)
#     print('내가 입력한 번호: ',end='')
    
#     for j in mylotto:
#         print('{}'.format(j),end=' ')
#     print()
#     # 입력한 번호가 나타나게
#     # print('내가 입력한 번호: ', mylotto)        
#     print('-'*30)

#-------------------------------------------------------   


# 번호 맞추기, 당첨확인
for num in mylotto:
    if num in lotto:
        mycount+=1
        okNum.append(num)


print('로또번호: ',end='') 
for i in lotto:
    print('{}'.format(i),end=' ')
print()
print('당첨번호: ',end='') 
for i in okNum:
    print('{}'.format(i),end=' ')
print()
print('입력번호: ',end='') 
for i in mylotto:
    print('{}'.format(i),end=' ')
print()
print('당첨개수:', mycount)
print('당첨금액:', reward[mycount])

    


# # 0~44까지 리스트
# lotto =[i+1 for i in range(45)]

# shuffle(lotto)  
# sample(lotto, 6)
# print(sample(lotto,6)) #랜덤으로 6개
# print(lotto)



# for i in range(500):
#     rno=randint(0,44) 
#     lotto[0],lotto[rno]=lotto[rno],lotto[0] # 1~45까지 이미 지정해놨기때문에 중복되지않음 ==> if문 필요없음

# print(lotto)



# # 6개의 수를 뽑아보세요.
# lottoNum=[]
# for i in range(6):
#     rno=randint(0,44)
#     lottoNum.append(lotto[rno])
# # ==> 중복숫자 발생

# # 6개의 수를 뽑아보세요.
# count=0
# lottoNum=[]
# while True:
#     if count<6:
#         rno=randint(0,44)
#         if not lotto[rno] in lottoNum:
#             lottoNum.append(lotto[rno])
#             count+=1
#     break            

# print(lottoNum)


# lotto=[]
# for i in range(45):
#     lotto.append(i+1)

# lotto=range(1,46)
# print(list(lotto))
# print(type(lotto))



# # random(): 0<= random() <1 , float형태이다
# print(random())
# print(random()*10) # 0*10<= random() <1*10
# print(random()*10+1) # 0*10+1<= random() <1*10+1

# # random()함수로 1~45 숫자 1개를 출력
# print(int(random()*45)+1)
# print(randint(1,45)) # 훨씬 간편함, 자바에서는 따로 int를 해줘야함


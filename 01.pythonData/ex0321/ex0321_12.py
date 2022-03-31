# 로또 맞추기 게임
# 로또 6개 생성 --> 1-45를 list에 입력하고, 
# list를 섞기해서 list순차적으로 6개를 뽑아서 로또 6개를 생성하시오.
# 입력 6개 생성
# 로또 번호와 입력번호 확인
# 똑같은 로또 번호 개수, 번호를 출력하시오.

from random import *
import test # import하고 싶은 파일이름을 넣어주면 됨



randNum=[]
randNum.append(10)
# 1-45까지 랜덤숫자 생성
test.lottoNum(randNum) # 호출에 변수를 넣었기 때문에 주소가 복사됨
print(randNum)



# # 로또 숫자생성 함수
# def lottoNum(randNum): # 함수안에서 randNum값이 어떤 것인지 확인하려면 함수 호출값을 기입해줘야함, return을 해주지않으면 호출해도 값이 바뀌지 않음
#     # #로또 1-45 리스트
#     # for i in range(45):
#     #     randNum.append(i+1)
#     randNum[0]=10
#     # tempNum=[0] # 광역변수를 선언하지 않았기 때문에 지역변수로 함수밖을 나가면 사라짐
    
# def tempLotto():
#     randNum[0]=500


# # 리스트이기때문에 randNum 선언하고 함수에서 숫자를 생성한뒤 출력함, \
# # 리스트가 아니라 변수이면 함수안에서 값을 바꿔도 함수내에서만 실행이 가능하기 때문에 결론적으로 값이 변경되지 않는다
# # 단 return으로 변수를 돌려주면 함수안에서 변경된 값을 적용할 수 있다
# randNum=[0] 

# lottoNum(randNum)
# randNum=lottoNum(randNum) # 함수에서 변경된 변수값을 적용하려면 다시 변수선언을 해서 덮어씌움

# tempLotto()
# print('로또숫자리스트 : ',randNum)

# # 로또 번호 생성하기
# randNum=[i for i in range(1,46)] 
# for i in range(500):
#     rno=randint(0,44)
#     randNum[0],randNum[rno]=randNum[rno],randNum[0]
    
# lotto=randNum[:6]



# # 입력번호 생성
# my_num=[]
# for i in range(6):
#     input1=int(input('{}번째 로또 번호를 입력하세요.>> '.format(i+1)))
#     my_num.append(input1)

# ok_num=[]
# ok_count=0    
# for i in range(6):
#     if my_num[i] in lotto:
#         ok_count+=1
#         ok_num.append(my_num[i])
        

# print('로또번호 : ', lotto)
# print('입력번호 : ', my_num)
# print('맞춘개수 : ', ok_count)
# print('맞춘번호 : ', ok_num)
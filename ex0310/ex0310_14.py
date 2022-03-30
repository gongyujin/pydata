from random import *

num = randint(1, 45) #1부터 100까지 숫자를 랜덤으로 뽑아줌

# count 5번 되면 빠져나오는 것
# count=1 # 반복횟수 변수
# while True:
#     input1= int(input('{}번째 도전! 숫자를 입력하세요.>> '.format(count)))
#     # 조건문 입력한 숫자와
#     if num==input1:
#         print('-'*60)
#         print('정답입니다.!'*5)
        
#         print('{}번째 도전: 숫자가 일치합니다. \n 입력한 숫자: {}\n 랜덤숫자: {}'.format\
#             (count,input1,num))
        
#         print('-'*60)
        
#         break # while 문을 빠져나옴.
#     else:
#         if count!=5:
#             print('-'*60)
            
#             print('{}번째 도전: 숫자가 일치하지 않습니다. \n 입력한 숫자: {}'.format\
#                 (count, input1))
            
#             print('-'*60)
#         else:
#             print('-'*60)
#             print('틀렸습니다.!'*5)
            
#             print('{}번째 도전: 숫자가 일치하지 않습니다. \n 입력한 숫자: {}\n 랜덤숫자: {}'.format\
#             (count,input1,num))
            
#             print('-'*60)
#             break
#         count+=1
            
    
count=1 # 반복횟수 변수
while True:
    
    if count<=5:
        input1= int(input('{}번째 도전! 숫자를 입력하세요.>> '.format(count)))
        # 조건문 입력한 숫자와
        if num==input1:
            print('-'*60)
            print('정답입니다.!'*5)
            
            print('{}번째 도전: 숫자가 일치합니다. \n 입력한 숫자: {}\n 랜덤숫자: {}'.format\
                (count,input1,num))
            
            print('-'*60)
            
            break # while 문을 빠져나옴.
        else:
            print('-'*60)
            
            print('{}번째 도전: 숫자가 일치하지 않습니다. \n 입력한 숫자: {}'.format\
                (count, input1))
            
            print('-'*60)
            count+=1
    else:
        print('-'*60)
        print('틀렸습니다.!'*5)
        print('5번을 실행하셨습니다. 프로그램 종료')
        print('랜덤숫자: {}'.format(num))
        
        print('-'*60)
        break
    


# input1= int(input('숫자를 입력하세요.>> '))

# if input1>100:
#     print('100보다 큰 수를 입력하셨습니다.')
# else:
#     print('100보다 작은 수를 입력하셨습니다.')
    
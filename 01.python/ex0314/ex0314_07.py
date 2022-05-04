from random import *

# randrange(1,100): 100전까지
# randint(1,100): 100까지

#1,100까지의 랜덤숫자 생성
#정답이 출력될때 지금까지 입력한 숫자를 출력하시오.
temp=randint(1,100)
   
count=0
my_num=[]
while count<10:
    
    print('-'*30)
    input1=int(input('{}번째 입력, 1-100사이의 원하는 번호를 입력하세요.>> '.format(count+1)))
    my_num.append(input1) #list에 숫자 저장
    print('-'*30)
    if temp == input1:
        print('정답입니다. 정답숫자 : {}'.format(input1))
        break
    elif temp>=input1:
        print('입력한 {} 숫자가 더 작습니다. 더 큰 수를 입력하세요.!'.format(input1))
    else:
        print('입력한 {} 숫자가 더 큽니다. 더 작은 수를 입력하세요.!'.format(input1))
    count+=1

if count ==10:
    print('틀렸습니다. 정답숫자 : {}'.format(temp))
    
    
#sort: 순차정렬, reverse: 역순정렬
my_num.sort(reverse=True) # 정렬한 값을 출력하고 싶다면 한번에 정렬+출력을 하면 안되고 정렬을 먼저 한 뒤에 출력을 해야함
print('입력한 숫자 : {}'.format(my_num))

    
# my_num=[]
# count=1
# while True:
#     if count<=10:
#         print('-'*30)
#         input1=int(input('{}번째 입력, 1-100사이의 원하는 번호를 입력하세요.>> '.format(count)))
#         print('-'*30)
        
#         my_num.append(input1)
#         if temp == input1:
#             print('정답입니다. 정답숫자 : {}'.format(input1))
#             break
#         elif temp>=input1:
#             print('입력한 {} 숫자가 더 작습니다. 더 큰 수를 입력하세요.!'.format(input1))
#         else:
#             print('입력한 {} 숫자가 더 큽니다. 더 작은 수를 입력하세요.!'.format(input1))
#         count+=1
#     else:
#         print('틀렸습니다. 정답숫자 : {}'.format(temp))
#         break

# my_num.sort()
# print('입력한 숫자: {}'.format(my_num))
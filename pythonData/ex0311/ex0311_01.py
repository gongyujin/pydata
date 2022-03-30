# # 입력받음 (input) : string형 ==> int형으로 바꿔줘야함
input1=int(input('점수를 입력하세요.>> '))

if input1>=90:
    print('A',end='') #end=''를 해줘야 자동으로 엔터키 설정이 안되고 바로 옆에 커서가 있어서 다음 문자를 이어서 쓸 수 있다
    if input1>=98:
        print('+')
    elif 93>=input1>=90:
        print('-')
elif input1>=80:
    print('B', end='')
    if input1>=88:
        print('+')
    elif 83>=input1>=80:
        print('-')
elif input1>=70:
    print('C', end='')
    if input1>=78:
        print('+')
    elif 73>=input1>=70:
        print('-')
elif input1>=60:
    print('D', end='')
    if input1>=68:
        print('+')
    elif 63>=input1>=60:
        print('-')
else:
    print('F')


# # 60점이상이면 합격, 미만이면 불합격
# if input1>=60:
#     print('합격입니다.')
# else:
#     print('불합격입니다.')
      
    
# if input1> 10:
#     print('10보다 큽니다.')
# else:
#     print('10보다 작습니다.')


# # 짝수입니다./ 홀수 입니다.
# if input1%2==0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')
          
# input1 = int(input('숫자를 입력하세요.>>'))

# # 3의 배수
# if input1%3==0:
#     print('3의 배수입니다.')
# else:
#     print('3의 배수가 아닙니다.')

# #5보다 크고 10보다 작은수 비교
# if 5< input1 <10:   # 5<input1 and input1<10:
#     print('5보다 크고 10보다 작은 수 입니다.')
    
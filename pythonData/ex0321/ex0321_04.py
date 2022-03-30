def coffee_machine(choice):
    print('[ 커피 주문완료 ]')
    print('1. 종이컵 준비')
    print('2. 물을 보충합니다.')
    print('3. 커피를 내립니다.')

    if choice==1:
        print('4. 커피를 컵에 추가합니다.')
        print('아메리카노 완성!!')
    elif choice==2:
        print('4. 커피를 한번 더 내린 후 컵에 추가합니다.')
        print('아메리카노2샷 완성!!')
    elif choice==3:
        print('4. 커피를 컵에 추가하고, 얼음을 보충합니다.')
        print('아메리카노(ice) 완성!!')
        
    print('포장을 한 후 진동벨을 누릅니다.')


while True:
    
    chocie=0
    print('1.아메리카노 2.아메리카노2샷 3.아메리카노(ice)')
    choice=int(input('커피를 선택하세요. (0: 프로그램 종료)>> '))
    if choice==0:
        print('프로그램을 종료합니다.')
        break    
    coffee_machine(choice)


# def mul(num1,num2):
#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)


# for i in range(3):
#     input1=int(input('숫자를 입력하세요.>> '))
#     input2=int(input('숫자를 입력하세요.>> '))
#     mul(input1,input2)



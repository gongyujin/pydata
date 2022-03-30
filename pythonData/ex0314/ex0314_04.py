# 두 수를 입력받아 사칙연산이 되도록 프로그램 하시오.
# 무한 반복할 수 있도록 합니다.

# while True:
#     num1=int(input('첫번째 수를 입력하세요.>> '))
#     num2=int(input('두번째 수를 입력하세요.>> '))
#     print('-'*25)
#     print('{} + {} = {}'.format(num1, num2, num1+num2))
#     print('{} - {} = {}'.format(num1, num2, num1-num2))
#     print('{} * {} = {}'.format(num1, num2, num1*num2))
#     print('{} / {} = {:.2f}'.format(num1, num2, num1/num2))
#     print('')
    
# 2번까지 실행할 수 있게 하고, 2번이후에는 지금까지 입력한 값을 출력해보세요.

# count=1
# arr=[]
# while count<=2:
#     num1=int(input('첫번째 수를 입력하세요.>> '))
#     num2=int(input('두번째 수를 입력하세요.>> '))
    
#     arr.append([num1,num2])
    
#     print('-'*25)
#     print('{} + {} = {}'.format(num1, num2, num1+num2))
#     print('{} - {} = {}'.format(num1, num2, num1-num2))
#     print('{} * {} = {}'.format(num1, num2, num1*num2))
#     print('{} / {} = {:.2f}'.format(num1, num2, num1/num2))
#     print('')
#     count+=1

# for i in range(len(arr)):
#     print('{}번째 입력 수 :'.format(i+1), arr[i])


#------------------------------------


# list 깊은 복사 # 새로운 공간을 만들어서 생성
list1=[[0]*2 for _ in range(5)]

# list 앝은 복사
# [[0]*2]*5 #주소값 동일(동일한 공간을 사용)

tempnum=0
while True:
    if tempnum <len(list1):
        num1=int(input('첫번째 수를 입력하세요.>> '))
        num2=int(input('두번째 수를 입력하세요.>> '))
        
        list1[tempnum][0]=num1
        list1[tempnum][1]=num2

        
        print('-'*25)
        print('{} + {} = {}'.format(num1, num2, num1+num2))
        print('{} - {} = {}'.format(num1, num2, num1-num2))
        print('{} * {} = {}'.format(num1, num2, num1*num2))
        print('{} / {} = {:.2f}'.format(num1, num2, num1/num2))
        print('')
        tempnum +=1
    else:
        tempnum +=1
        break
    
print('첫번째 입력 수 :', list1[0])
print('두번째 입력 수 :', list1[1])
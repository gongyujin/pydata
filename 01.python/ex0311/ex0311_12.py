# 두수를 입력받아 홀수의 값의 합을 출력하시오.
# ex) 1,10 -> 홀수의 합을 구하면 됨. 1,3,5,7,9의 합

num1 = int(input('첫번째 숫자를 입력하시오.>> '))
num2 = int(input('두번째 숫자를 입력하시오.>> '))

sum1=0
for i in range(num1, num2+1):
    if i %2==1:
        sum1+=i
print('{}부터 {}까지 홀수의 합 : {}'.format(num1,num2,sum1))
        




# # 0-100 7의 배수의 합을 구하시오.
# num1=0 #합을 구하는 변수
# for i in range(0,101):
#     if i%7==0:
#         num1+=i
# print('0부터 100까지 7의 배수의 합 :', num1)


# #0-100 홀수의 합을 구하시오.
# num2=0
# for i in range(0,101):
#     if i %2==1:
#         num2+=i
        
# print('0부터 100까지 홀수의 합 :', num2)
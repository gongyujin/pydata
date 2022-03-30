from math import *
# 10.275 올림
print(ceil(10.275))

# a= 10.275
# 소수점 3자리 반올림 10.28
a= 10.275
print(round(a*100)/100)
print(round(a,2))

# max(10,3) # 최대값
# print(max([10,3,7]))

# min(10,3) # 최소값

# print(abs(-5)) # 절대값

# print(pow(4,3)) #제곱근

# print(round(4.51)) #반올림
# print(round(3.49)) #반올림

# print(floor(12.9)) #버림 ------> 기본함수가 아니여서 math를 import해야함
# print(ceil(14.1)) #올림

# # 두수를 입력받아 작은수부터 출력하시오.
# # 10, 5 --> 출력 : 5,10

# num1=int(input('첫번째 숫자를 입력하세요.>> '))
# num2=int(input('두번째 숫자를 입력하세요.>> '))

# if num1 < num2:
#     print('출력: {}, {}'.format(num1,num2))
# else:
#     print('출력: {}, {}'.format(num2,num1))
    
# # 5개를 입력받아 순차적으로 입력하세오.

# num=[]
# for i in range(5):
#     a=int(input('{}번째 숫자를 입력하세요.>> '.format(i+1)))
#     num.append(a)
    
# num.sort(reverse=True)
# for i in num:
#     print(i,end=' ')

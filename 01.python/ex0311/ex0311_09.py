# 두개의 숫자를 입력해서 두 값사이의 모든 값을 더하라
# 숫자 입력 1,10 :1,2,3,4,5,6,7,8,9,10까지 더해라
num1=int(input('숫자를 입력하세요.'))
num2=int(input('숫자를 입력하세요.'))

# num1, num2 비교
if num1 > num2:
    a= num1
    num1=num2
    num2=a
    # num1,num2=num2,num1 :한줄로 쓸수 있음

sum = 0 #전역변수
for i in range(num1,num2+1): 
    sum = sum + i
    
print('총합 :', sum)


# sum = 0 #전역변수
# for i in range(num1,eval(num2)+1): #eval 문자를 숫자로 변경해주는 함수
#     sum = sum + i
    
# print('총합 :', sum)
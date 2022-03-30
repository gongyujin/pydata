# a=int(input('숫자를 입력하세요.>>'))
# b=int(input('숫자를 입력하세요.>>'))

# # 더하기, 빼기, 곱하기, 나누기를 출력하시오.
# print(a, '+', b, '=', a+b)
# print(a, '-', b, '=', a-b)
# print(a, '*', b, '=', a*b)
# print(a, '/', b, '=', a/b)
# print('{} / {} = {:.2f}'.format(a,b,a/b))

# a='100'  #'100'을 int나 float로 바꿀수 있지만 '100name'과 같이 조합되어 있으면 변환할 수 없음
# print(int(a)+100)


a= int(input('첫번째 숫자를 입력하세요.>> '))
b= int(input('두번째 숫자를 입력하세요.>> '))

print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {}'.format(a,b,a/b))
print('-'*20)

sub1=int(input('국어 점수를 입력하세요.>> '))
sub2=int(input('영어 점수를 입력하세요.>> '))
sub3=int(input('수학 점수를 입력하세요.>> '))

print('합계 :', (sub1+sub2+sub3))
print('평균 : {:.2f}'.format((sub1+sub2+sub3)/3))
print('-'*20)

num1=int(input('첫번째 숫자를 입력하세요.>> '))
num2=int(input('두번째 숫자를 입력하세요.>> '))

print(num1/num2)
print(num1//num2)
print(num1%num2)
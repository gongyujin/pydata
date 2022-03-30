# 빈공백 제거하는 방법
in_str=input('아이디를 입력하세요.>> ')
com_str=in_str.replace(' ','')
print('아이디: {}'.format(com_str), end='-----')
print()

str1='                             aa  bb  cc                  '
print(str1.rstrip()) #오른쪽 공백없애기
print(str1.lstrip()) #왼쪽 공백없애기
print(str1.strip()) #양쪽 공백없애기
print(str1.replace(' ','')) #공백없애기

# # 숫자의 단위, 없애기
# str1='123,450,000'
# num1=10000

# #123450000
# num2=int(str1.replace(',','')) # 웹에 들어가 있는 숫자 통계는 거의 ,가 들어가 있음
# print('{:,}'.format(num1+num2))


# str1='서울인재개발원은 서울에 있습니다. 서울은 동아시아권입니다.'

# print(str1.replace('서울','한국')) # a,b : a를 b로 바꿔줌
# print(str1.replace('서울','')) # 다 지워질수 있음


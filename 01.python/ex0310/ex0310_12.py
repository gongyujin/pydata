# 예) 234568000
# 돈을 입력받아 5만원권, 1만원, 5천원, 1천원 교환해서 출력하시오.

money = int(input('교환할 돈의 금액을 입력하세요.>> '))

# 5만원권 234568000 --> 4691*50000: 나머지 18000원
p50=money//50000
# 1만원권 18000 --> 1*10000: 나머지 8000원
p10=(money%50000)//10000
# 5천원권 8000 --> 1*5000: 나머지 3000원
p5=((money%50000)%10000)//5000
# 1천원권 3000 --> 3*1000: 나머지 0원
p1=(((money%50000)%10000)%5000)//1000

print('교환할 돈의 금액 :', money)
print(format(money,',')) #변수에 ,를 포함해서 숫자를 저장해주면 타입이 에러가 나기때문에 변수에는 , 빼서 저장해주고 print할때 , 를 해줘야함
print('{:,}'.format(money))
print('5만원권 :', p50 ,'장')
print('1만원권 :', p10 ,'장')
print('5천원권 :', p5 ,'장')
print('1천원권 :', p1 ,'장')


a=10000
b='10,000'
c=b.replace(',','') # ,를 첨부하면 세상복잡하게 계산해야함
print(a+int(c))
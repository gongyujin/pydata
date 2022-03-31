total,i=0,0 #광역변수로 출력하고 싶을때는 반드시 초기값을 선언해줘야함

for i in range(1,100):
    total+=i
    print('{},{}'.format(i,total))
    if total > 100:
        break
    
print('합 : {}'.format(total))
print('100을 넘었을 때 숫자 :', i)
print('100을 넘기 전 숫자 :', i-1)

# a= input('문자를 입력하세요.')

# if a== '$':
#     print('$ 문자입니다.')
# else:
#     print('$ 문자가 아닙니다.')
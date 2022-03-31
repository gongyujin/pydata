# 반복문 내부에 if 조건문의 조건식을 채워서 100 이상의 숫자만 출력하시오.

numbers=[273, 103, 5, 32, 65, 9 ,72, 800, 99]

for num in numbers:
    if num >= 100:
        print('100 이상의 수: ', num)
print()


chk=['짝수','홀수']
for num in numbers:
    # if num % 2 ==0:
    #     print('{:3d}: 짝수'.format(num))
    # else:
    #     print('{:3d}: 홀수'.format(num))
    # print()
    
    print('{:3d}: {}'.format(num,chk[num%2]))

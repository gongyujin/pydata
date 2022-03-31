#입력한 단 부터 입력한 단까지 출력하시오. 

num1=int(input('숫자를 입력하시오.>> '))
num2=int(input('숫자를 입력하시오.>> '))

if num1>num2:
    num1,num2=num2,num1


for i in range(num1,num2+1):
    print('[ {} ]단'.format(i))
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j))

#-------------------------------------------------------

for i in range(1,10):
    # print('[ {} ]단'.format(i))
    for j in range(num1,num2+1):
        print('{} * {} = {}  '.format(j,i,i*j), end='')
    print()




# for i in range(1,10):
#     # print('[ {}단 ]'.format(i))
#     for j in range(2,10):
#         print('{} * {} = {}   '.format(j,i,j*i), end='')
#     print()    
#0-100, 짝수만 list에 넣어보세요.
num1=[];
num2=[];
for i in range(0,101):
    if i%2==0:
        num1.append(i)
    else:
        num2.append(i)

print('짝수 \n{}'.format(num1))
print('홀수 \n{}'.format(num2))

# list 1부터 100까지 들어가는 리스트를 for문으로 출력하시오.

# num_list=[]
# for num in range(0,101):
#     num_list.append(num)
    
# print(num_list)

# num=[i for i in range(0,101)] #한줄로 만들수 있음
# print(num)


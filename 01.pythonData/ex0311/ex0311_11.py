for i in range(0,10,3):  #(10,0,-1): 10부터 -1씩 감소하겠다는 뜻
    print(i)


# range(1,2,1) : for문에서 범위를 지정하는 것
# [0,1,2]: for문에서 리스트에 있는 것을 가져오는 것

numbers =[3,4,5,2,1]
for number in numbers:
    print(number)
    
for i in range(10):
    print(i)


# a=0
# if a>5:
#     pass #pass를 써주지않고 빈공간으로 두면 error가 발생하기 때문에 pass를 써줘야함
# else:
#     print('5보다 작습니다.')
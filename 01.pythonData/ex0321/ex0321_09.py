# para_func함수 생성, 가변매개변수를 사용해서 
# 매개변수 합, 매개변수 모든값을 리턴해서

# 호출한 곳에서 값을 출력하시오.
# para_func(10,20,30,40,50,60,70,80,90,100)

# 출력
# 매개변수 합: 1111
# 매개변수 값: 10,20,30,40 .... 100

# 옵션
# 매개변수값을 입력받아, 받고 싶은 만큼 받아서 출력

# def para_func(*para):
#     total=0
#     temp=[]
#     for i in para:
#         total+=i
#         temp.append(i)
#     return total, temp

# data=para_func(10,20,30,40,50,60,70,80,90,100)
# print('매개변수 합 : ', data[0])
# # print('매개변수 값 : ', data[1])
# for i in data[1]:
#     if i == data[1][0]:
#         print('매개변수 값: ', i, end='')
#     else:
#         print(',',i,end='')
# print()
#-------------------------------------------
def para_func(num,*para): # 키와 value가 같이 있으면 가변 *을 두개 붙여줘야함, * 하나만 있는 것은 value 만을 의미함
    total=0
    temp=[]
    for i in num:
        total+=i
        temp.append(i)
    return total, temp

num=[]
while True:
    temp_num=int(input('숫자를 입력하세요. (0: 프로그램종료)>> '))
    if temp_num==0:
        print('매개변수 입력종료')
        break
    num.append(temp_num)

data=para_func(num)
print('매개변수 합 : ', data[0])
# print('매개변수 값 : ', data[1])
for i in data[1]:
    if i == data[1][0]:
        print('매개변수 값: ', i, end='')
    else:
        print(',',i,end='')
print()



# # def 함수이름() 함수선언
# # (매개변수1, 매개변수2) : 매개변수는 호출개수와 함수선언의 매개변수 개수가 같아야함
# # 매개변수 기본값설정, 매개변수에 디폴트값을 설정할수 있음. 예) v3=10
# # 기본값 설정이 되어 있는 매개변수는 호출에서 값이 입력되지 않으면 기본값이 세팅이 됨.
# # return 개수는 상관없음 리턴변수는 2개이상일때 튜플타입, 없으면 생략가능

# # 디폴트 매개변수값, 가변매개변수를 사용하면 개수가 맞지않아도 실행됨
# def para_func(v1,v2,*para,v3=0): #가변에는 다양하게 사용할 수 있음
#     print('v1 : ', v1)
#     print('v2 : ', v2)
    
#     for i in para:
#         print('para : ', i)
#     # print(para[0]) # 하나만 print하고 싶을때
#     print('v3 : ', v3)
#     return

# para_func(1,2) # 호출하는 개수 맞춰야함, *para나 디폴트값은 개수 맞춰주지 않아도 됨
# print('프로그램 실행완료')
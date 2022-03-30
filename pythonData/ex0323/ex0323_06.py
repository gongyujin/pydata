# 입력한 값을 +10을 만들어서 출력하시오.
# lambda함수 만들어 출력하시오.
# def add10(num):
#     return num+10

# 람다함수 뒤 매개변수 출력가능
# #1
# add10=lambda num:num+10
# print(add10(10))
# #2 : 1번을 한줄로 표현할 수 있음
# print((lambda num:num+10)(10))
# # 두개 매개변수
# print((lambda num,num2:num+num2+10)(10,20))


list1=[9,5,6,4,5,1,7,3,9,10]
list2=[0,1,0,0,1] # true false로 인식
list3=['','aaa','','a',''] # 아무것도 없으면 false, 글자있으면 true

for i in list2:
    if i==True:
        print(i,'True')
    else:
        print(i,'False')

# for i in range(len(list1)):
#     list1[i]=(lambda num:num+10)(list1[i])
    
# print(list1)

# print(list(map(# 람다함수,list1)))
print(list(map(lambda num:num+10,list1)))

# 조건에 해당되는 데이터값을 리스트로 넘겨줌
print(list(map(lambda num:num%2,list1))) # filter대신 map이 들어가면 num%2의 결과값을 보여줌

print(list(filter(lambda num:num%2==0,list1)))

# # 1-100 더하기 함수를 만들어서 출력하시오.
# # lambda함수 만들어 출력하시오
# def addNum(num1,num2):
#     sum=0
#     for i in range(num1,num2+1):
#         sum+=i
#     return sum

# print(addNum(1, 100))

# def hap(num1,num2):
#     result=num1+num2
#     return result

# hap(1,2)

# # 함수이름 = lambda 매개변수1,매개변수2:실행문
# hap2 = lambda num1,num2:print(num1+num2) # 한줄로 줄일수 있음
# hap2(10,20)
# hap2(10,lambda num1,num2:print(num1+num2)) # 함수를 넣어줄수 있음


# # 함수선언
# def fun1(v1,v2): 
#     #내부함수선언 - 함수내에 함수를 정의
#     def fun2(num1,num2): # 내부함수 가능
#         return num1+num2
    
    
#     return fun2(v1,v2)


# print(fun1(10,20))
# print(fun2(10,20)) #내부함수는 따로 호출할수 없음
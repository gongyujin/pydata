def calc(num1,num2,choice):
    result=0 #초기화
    if choice==1:
        result=num1+num2
        
    return result
        


print('[ 사칙연산 프로그램 ]')
print('1.+ 2.- 3.* 4./')
choice = int(input('원하는 번호를 입력하세요.>> '))
num1=int(input('숫자를 입력하세요.>> '))
num2=int(input('숫자를 입력하세요.>> '))

result=calc(num1,num2,choice)
print(result)


# # def cal(v1,v2):
# #     result=[0,0,0,0] #자바에서는 같은 타입만 넣을수 있어서 불편
# #     result[0]=v1+v2
# #     result[1] =v1-v2
# #     result[2]=v1*v2
# #     result[3]=v1/v2
# #     return result
# #     # return v1, v2 # return이 두개로 나오면 튜플형태로 결과나옴

# # hap=cal(1,2)
# # print(hap)


# def cal(v1,v2): 
#     result=0
#     result =v1+v2
#     return result

# hap=cal(1,2) # 함수선언보다 위에다가 쓰면 import를 사용해서 쓰면 됨, 꼭 같은 파일안에서 선언해서 사용하지 않아도 됨
# print(hap)
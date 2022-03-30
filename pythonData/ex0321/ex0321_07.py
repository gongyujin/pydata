# 함수선언
def cal(v1): #들어간 myList값은 주소값이 들어간것
    # global을 선언하지 않아도 변수값을 바꿀 수 있음
    temp1=v1[0]
    temp2=v1[1]
    v1[0]=temp1+temp2
    v1[1]=temp1-temp2
    
# 전역변수
myList=[100,200]
# 함수호출
cal(myList)
print('더하기,빼기 값 :',myList[0],myList[1])


# def cal(v1,v2): # 매개변수에 hap, sub를 써버리면 에러가 남
#     global hap,sub # hap을 로컬로 쓸 수 있는데 global이 반드시 맨위에 있어야함
#     # hap=0
#     hap=v1+v2
#     sub=v1-v2
    

# # 전역변수
# hap,sub=0,0

# cal(100,200)
# print('더하기,빼기 값 :',hap,sub)



# def cal1():
#     global a
#     a=10 # global a에다가 10을 넣어줌; 전역변수 a를 호출해서 10을 넣어줌
    
    
# a=20 
# cal1() # 10으로 바뀜
# print(a)    
    
    

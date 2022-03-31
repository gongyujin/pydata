#함수: 사칙연산을 하는 함수
def cul(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

cul(100,5)
print('-'*20)
cul(50,2)

#변수 한개당 하나밖에 안됨, 여러개 변수를 만들기에는 힘듦 ==> 이 부분을 해결하기 위해서는 '리스트'를 사용하면 됨
num = [1,2,3,4,5] #리스트 ; 변수하나로 리스트만들기

#리스트와 함수를 한번에 커버하는게 클래스 ; 파일하나를 클래스라고 보면 됨


# # 200->50, 100-> 10, 10-> 30, 5-> 2
# a= 50  #변수사용해서 숫자변경해주면 됨/ 다른 숫자 여러개 할려면 함수사용해서 하면 된다
# b= 10
# c= 30
# d= 2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print('-'*20)
# print(c+d)
# print(c-d)
# print(c*d)
# print(c/d)
# print('-'*20)
# print(b+b)
# print(b-b)
# print(b*b)
# print(b/b)

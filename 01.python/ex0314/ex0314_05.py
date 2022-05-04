# a=1
# b=2
# c=a
# print(a) #1
# print(b) #2
# print(c) #1

# a=2
# print(a) #2
# print(c) #1

a=[1]
b=[2]
c=a #주소가 복사가 되는 것임
print(a)
print(b)
print(c)

a[0]=10 #a가 바뀌게 되면 복사본도 같이 바뀌게 됨
        # 변수=1은 하나만 저장되기 때문에 바로 입력되는데 변수이외에 모든것은 데이터를 저장하고 데이터가 저장된 주소를 불러옴
print(a)
print(c)
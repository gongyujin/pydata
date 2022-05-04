list1=[] #방을 추가해서 넣어줘도 됨
num1=int(input('숫자를 입력하세요.>> '))
list1.append(num1)

list2=[0,0,0,0] #방을 미리만들어서 채워주면 됨
nnum1=int(input('숫자를 입력하세요.>> '))
list2[0]=nnum1
# list2[5]=nnum1 #리스트에 없는 주소를 출력하면 에러남

print("list의 크기 : ",len(list2))
print("list의 최대 주소 : ",len(list2)-1)


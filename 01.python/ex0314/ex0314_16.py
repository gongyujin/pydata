aa=[1,2,3]
bb=[4,5,6]

cc=aa+bb # 숫자를 더하는 것이 아니라 리스트를 합체해줌
print(cc)

dd=aa*3 # aa가 3번 반복적으로 나타남
print(dd)

print(cc[::2]) # 두칸씩 띄어서 출력

print(cc[::-2]) #마이너스는 역순을 의미함
print(cc[::-1])

cc[0]=10
print(cc)

cc[1:2]=[20,21]
print(cc)
cc[1:3]=[50] # 슬라이스는 리스트 개수랑  상관없음, 리스트 개수를 일치  시키지 않아도 오류가 뜨지않음, 대신 부족하면 지정한 개수만큼만 변경됨
print(cc)
cc[1:2]=[50,40,30,20]
print(cc)

cc[5]=[1,2,3] # 특정적으로 지정하면 배열이 들어가게 됨
print(cc)



del(cc[0]) #공간이 남아있는게 아니라 그냥 날라가게 됨 ==> len 크기가 줄어듦
print(cc)

#빈공백으로 넣기
cc[2:4]=[]
print(cc)
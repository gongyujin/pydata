aa=[1,2,333,6,555,6,77,8,9]
print("1: ",aa)

# bb=aa.sort() # 정렬은 가능하지만 aa 정렬한것을 bb에 옮기는 것은 불가능함 ==> None 타입으로 나타나게 됨
# print("2: ",bb)
# print('--')
# cc=sorted(aa) # sort가 아닌 sorted 함수를 사용해야 다른 변수에 옮겨넣을 수 있다.
# print("3 :",cc)

# aa[0]=500
# print("4 :",aa) 
# print("5 :",cc) # 같은 주소를 사용하는게 아니기 때문에 aa를 변경하여도 cc가 같이 변경되지 않는다

#--------------------------------------------------------
# 얕은 복사는 주소값을 복사해서 aa가 바뀌면 bb도 바뀜
# bb=aa
# aa[0] =500
# print('aa list[aa[0]=500 : ',aa)
# print('bb list : ',bb) # 같은 주소가 복사 되어있기 때문에 aa가 변하면 bb도 같이 변함

# 깊은 복사 aa가 바뀌어도 bb는 바뀌자 않음.
# bb=aa.copy()
# aa[0] =500
# print('aa list[aa[0]=500 : ',aa)
# print('bb list : ',bb) #변수를 제외하고는 복사할때는 얕은 복사가 아닌 깊은 복사를 사용해줘야함
#----------------------------------------------------------------------

# # list로 추가
# aa.extend([1,2,3]) #append는 숫자 하나만 뒤에 추가할 수 있는데 extend는 여러숫자를 뒤에 이어서 추가할 수 있다.
# print(aa) 


# count= aa.count(6) # 찾고자하는 데이터의 개수를 알려줌
# print(count)

# aa.insert(2, 3) #insert(2,3): 2번자리에 3번을 삽입한다.
# print(aa)
# aa.append(44)
# print(aa)


# idx=aa.index(77) #찾는 데이터 위치를 알 수 있음
# print(idx)
# if 77 in aa:
#     print('77 값이 있습니다.')

# # 역순정렬
# aa.sort(reverse=True)
# print(aa)

# # 순차정렬
# aa.sort()
# print(aa)


# #일부 삭제
# aa.pop() # 번호 안넣으면 제일 마지막꺼 삭제
# aa.pop(3)
# print(aa)

#  # 데이터 값을 삭제
# # list의 데이터를 검색해서 리스트 삭제함
# for i in range(len(aa)):
#     if 6 in aa:
#         aa.remove(6)
# print(aa)

# aa.clear
# print(aa)
# print(type(aa))


# aa.remove(333)
# print(aa)

# pop: 제일 마지막꺼를 삭제할때 사용
# remove: 지정한 값을 삭제함

# #삭제방법1
# aa[1:4]=[]
# print(aa)

#삭제방법2
# aa=[] # 전체삭제
# print(aa)
# print(type(aa)) #리스트로 타입의 형태는 남아있음

#삭제방법3
# aa=None #완전 삭제
# print(aa)
# print(type(aa)) # 타입자체가 none임 : 타입이 없다는 것을 의미, 완전 없다, 변수만 존재함

#삭제방법4
# del(aa)
# print(aa) # aa이름이 아예없어짐, 변수가 아예 없어짐 ==> 출력하려고 하면 에러가 나게 됨, 변수자체도 제거


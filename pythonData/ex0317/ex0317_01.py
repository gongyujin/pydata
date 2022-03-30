stulist=[
    {'stuno':1,'stuname':'홍길동', 'kor':100,'eng':100,'total':100+100,'avg':100,'rank':0},
    {'stuno':2,'stuname':'이순신', 'kor':100,'eng':99,'total':100+99,'avg':(100+99)/2,'rank':0},
    {'stuno':3,'stuname':'유관순', 'kor':99,'eng':99,'total':99+99,'avg':(99+99)/2,'rank':0}
]
# stu1={'stuno':1,'stuname':'홍길동', 'kor':100,'eng':100,'total':100+100,'avg':100,'rank':0}


# for stu in stulist:
#     if '홍길동' == stu['stuname']:
#         print('홍길동이 있습니다.')
#         break

# print(type(stu1.values())) # 괄호안에 담겨져 있기때문에 list가 아님
# print(type(list(stu1.values()))) # 이렇게 하면 리스트

# if '홍길동' in stu1.values():
#     print('홍길동이 있습니다.')


while True:
    print(stulist)
    searchName=input('찾고자 하는 학생이름을 입력하세요.>> ')
    count=0
    for i, stu in enumerate(stulist):
        if searchName in stu.values(): 
            print('{}이 있습니다.'.format(searchName))
            del(stulist[i])
            print('{}이 삭제되었습니다.'.format(searchName))
            count=1
            break
        
    if count==0:
        print('{}이 없습니다.'.format(searchName))






# stu1={'stuno':1,'stuname':'홍길동', 'kor':100,'eng':100,'total':100+100,'avg':100,'rank':0}
# print(stu1['stuno']) # 웹에서는 stu1.stuno 형태로 입력
# print(stulist[0]['stuname'])

# studic={'stuno':1,'stuname':'홍길동', 'kor':100,'eng':100,'total':100+100,'avg':100,'rank':0}

# print(studic.items()) # 튜플형태

# # value값만 가져옴
# for v in studic.values():
#     print('{}'.format(v,end=' '))

# # 키값만 가져옴
# for k in studic.keys():
#     print('{}'.format(k,end=' '))
#     print(studic[k])  # value값만 찍힘  

# for k, v in studic.items():
#     print('{} : {}'.format(k,v,end=' '))
#     # print('{} : {}'.format(k,v),end=' ')


# a=1
# print(a)
# a=3
# print(a)

# #리스트
# list1=[1,{1:'aaa'},2,3,4,5] # java 배열과 비슷하지만 python에서는 리스트에 객체(모든타입)을 담을 수 있음
# list1[3]=5
# list1.append(7)
# print(list1)
# del(list1[3])
# print(list1)


# #튜플
# dtuple=(1,{1:'aaa'},2,3,4,5) # 리스트처럼 모든 타입을 담을 수 있음, 단 그 이후로는 수정이 안됨
# print(dtuple[0])
# # print(dtuple[0]=1) # tuple은 변경, 삭제, 추가가 안됨



# #딕셔너리
# datadic={1:'aaa',2:'bbb','id':'aaa'} # 튜플도 들어올수 있음
# print(datadic[1]) # 읽어오기

# datadic[1]='ddd' # 변경하기
# print(datadic)
# datadic['pass']='1111' # 추가하기
# print(datadic) 
# del(datadic[2]) # 삭제하기
# print(datadic)
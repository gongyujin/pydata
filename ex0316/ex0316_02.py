s=[1,'홍길동']
# dictionary 선언
stu1={'stu_no':1,'name':'홍길동','major':'컴퓨터공학과'}


print(stu1['name'])
print(stu1.get('name')) 

# print(stu1['tel']) # key값이 없으면 오류가 나기 때문에 확인해야함
print(stu1.get('tel')) # key 값이 없어도 오류가 나지않고 None으로 표시됨

# print하게 되면 리스트로 나오게 됨
print(stu1.keys()) 
print(stu1.values())

print(type(stu1.values()))
print(type(stu1.keys()))
print(list(stu1.values())) # 그냥 list형태로 출력할 수 있다
print(list(stu1.keys()))

print(stu1.items()) # 튜플형태로 나타남, 리스트안에 소괄호 형태로 나오게 됨, 튜플은 수정할 수 없음
# 수정을 하면 안되는 상황에서 튜플을 많이 사용함

print('name' in stu1) #if 'name' in stu와 같은 맥락/ stu는 리스트


# aa list에 11의 데이터가 있는지 확인
aa=[1,2,4,7,11,44,77]
if 11 in aa:
    print('11이 있습니다.')

# 딕셔너리에 name키가 있는지 확인
if 'name' in stu1:
    print('name value 값:', stu1['name'])
    print('name 키가 있습니다.')
else:
    print('name 키가 없습니다.')


# print(stu1['major']) # 문자열을 입력할때는 반드시 따옴표를 표시해야함
# print(stu1['stu_no'])
# print(stu1)


# s.append(100) # 리스트는 append로 추가
# # dictionary 추가
# stu1['tel']='010-0000-0000' # 딕셔너리는 그냥 추가해주면 됨, 새로운 key값 넣으면 걍 추가 됨
# print(stu1)

# # dictionary 삭제
# del(stu1['tel'])
# print(stu1)

# print(stu1['name'])

# stu_no :변수
# stuNo() : 함수
# StuNo : 클래스

# # 리스트와 딕셔너리의 차이: 1. 대괄호, 중괄호 차이 2. key가 같이 나오느냐 안나오느냐
# stu=[1,'홍길동',100,100,200,100.0,0] #리스트 , 리스트안에 요소가 어떤 것을 나타내는지 모름
# aa={'no':1, 'name':'홍길동','kor':100,'eng':100,'total':200} # 각 요소가 어떤 것을 뜻하는지 알려줌, dictionary 앞에 문자가 들어가도 되고 숫자가 들어가도 됨
# aa2={0:1, 1:'홍길동'}
# print(aa)
# print(aa2)
# print(aa2[1])
# print(aa['name'])
# # key는 유일해야하므로 중복이 되면 안됨 (key값이 중복되면 맨마지막 값으로 덮어씌움), 대신 value는 중복가능
# # value값에는 리스트가 들어와도 되고, 딕셔너리가 들어와도 괜찮음

# aa=[
#     [1,2,3,4],
#     [5,6],
#     [7,8,9]
#     ]

# # print('13의 리스트 위치 주소 :',aa.index(13))

# for a2 in aa:
#     for a in a2:
#         print(a)
    

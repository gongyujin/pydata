foods=['떡볶이','짜장면','라면','피자','맥주']
sides=['오뎅','단무지','김치','피클','땅콩']

# 얕은 복사
# # 1개의 주소값으로 2개가 동시에 사용되어짐
# foods2=foods
# foods2[0]='안팔어'
# print(foods) # 주소가 같기때문에 같이 변경됨

# 깊은 복사
# # 복사할땐 copy 명령어를 사용
# foods2=foods.copy()
# foods2=foods[:] # 주소를 복사하는 것이 아니기때문에 슬라이스로 긁어와서 넣어주는 느낌임, copy랑 같다
# foods2[0]='안팔어'
# print(foods) # 주소가 같기때문에 같이 변경됨



# # 튜플형태의 list타입으로 변경
# # 2개의 list를 dic타입으로 변경
# tuplist=list(zip(foods,sides))
# print(type(tuplist))
# dic=dict(tuplist)
# print(type(dic))
# print(dic)

# zip: 두개이상일때 표시해줌
for food, side in zip(foods, sides): #zip을 사용하지 않으려면 2중코드를 돌려야함
    print('{} : {}'.format(food,side))

# # min: 최소값을 리턴 max: 최대값을 리턴
# idx=min(len(foods),len(sides)) #len(foods),len(sides)는 매개변수

# # dis=0
# # if len(foods)<len(sides):
# #     dis=len(foods)
# # else:
# #     dis=len(sides)

# for i in range(idx):
#     print('{} : {}'.format(foods[i],sides[i]))


# complist=[0,1,2,3,4,5,6,7,8,9]
# complist=[3,6,9,12,15,18]

# for문의 종류

# # 기본 for문
# alist=[]
# for i in range(0,10):
#     alist.append()

# # 한줄 for문
# alist=[i for i in range(0,10)]

# # 1-20 3의배수만 입력
# # 기본 for문
# alist=[]
# for i in range(1,21):
#     if i % 3 ==0:
#         alist.append(i)
# # 한줄 for문
# alist1=[i for i in range(1,21) if i %3 ==0]

# print(alist)
# print(alist1)
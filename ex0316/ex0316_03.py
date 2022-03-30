# 전체적으로 내부적으로는 클래스 기반으로 만들어져 있음

aa=[1,'홍길동',100,100,200,100.0,0]

for i in aa: #i:1,'홍길동',100,100,200,100.0,0
    print(i) 
for i in range(len(aa)): #i:0,1,2,3,4,5,6
    # print(aa[i])
    print('{} : {}'.format(i,aa[i]))

stu1={'no':1,'name':'홍길동','kor':100,'eng':100,'total':200,'avg':100.0,'rank':0}

for key in stu1:
    print('{:5s} : {}'.format(key, stu1[key]))

# while True:
#     search=input('키값을 입력하세요.>> ')
#     if search in stu1:
#         print(stu1[search])
#     else:
#         print('키값이 없습니다. 다시 입력하세요,!!')
#         print()
# 학생관리폴더 : 학번, 이름, 전화번호, 주소, 성별, 학년, 학과
# 학생성적폴더 : 학번, 국어, 영어, 수학, 합계, 평균, 등수
# 학번이 공통이기 때문에 key로 쓸수 있음
from stumanage.studef_test import *

while True:
    # 화면출력
    choice=screenPrint()

    if choice==1:
        stuInput() # 학생성적입력
    
    elif choice==2:
        stuoutput() # 학생전체출력
        
    elif choice==3:
        stuSearch() # 학생검색출력
        
    elif choice==4:
        stuModify() # 학생성적수정
        
    elif choice==5:
        stuDelete() # 학생성적삭제       
        
    # elif choice==6:
    #     stuRank() # 학생등수처리
    
    elif choice==0:
        print('프로그램을 종료합니다.')
        break









# s1=Student(1, '홍길동', 100, 100)
# s2=Student(2, '이순신', 100, 100)
# s3=Student(3, '홍길동', 100, 100)

# if s1==s3: # s1.stuname이라고 쓰지 않아도 됨
#     print('두 객체는 같습니다.')
# else:
#     print('두 객체는 다릅니다.')


# s=Student(1, '홍길동', 100, 100)

# # s.kor=-100
# s.setKor(200)
# # s.__kor=-100 # 프라이빗이 인식이 되는 이유는 __를 변수로 인식해버려서


# # print('{},{}'.format(s.stuname,s.__kor)) # __kor 변수선언한것을 데려옴 ; -100
# print('{},{}'.format(s.stuname,s.getKor())) # setKor 에서 데려옴; 200
# print('{},{}'.format(s.stuname,s.kor)) # 100
# # print(s.__kor)
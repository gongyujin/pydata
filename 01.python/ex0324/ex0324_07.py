# 학생성적프로그램
# 입력, 출력
# ex0324_07.py -main
# stu_class.py : 객체 클래스
# stu_func.py : 함수사용
from stu_func import *
import stu_class
import json

# stuSave=[] # 저장형태는 class를 사용할 것
while True:
    choice=0
    choice=screen_print()
    
    if choice==1:
        stu_input()
        
    elif choice==2:
        stu_print()
    
    elif choice==3:
        pass
    elif choice==0:
        print('프로그램을 종료합니다.')
        break


print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
for stu in stuSave:
    print(stu)
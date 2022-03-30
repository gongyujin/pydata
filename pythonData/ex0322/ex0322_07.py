# # 학생성적프로그램
# # 3명의 학생의 성적을 입력받아 번호, 이름, 국어, 영어, 합계, 평균, 등수

# # [ 학생성적프로그램 ]
# # 1. 학생성적입력
# # 2. 학생파일저장
# # 3. 학생파일읽기
# # 4. 학생성적모두 출력
# #---------------------------
# # 원하는 번호를 입력하세요.
# # 3명 입력
# # 1명 더 입력
# # 파일저장
# # 파일읽기
# # 1명 더 입력
# # 학생성적모두출력
# # 파일저장
# stuSave=[]
# count=0
# while True:
#     print('[ 학생성적프로그램 ]')
#     print('1. 학생성적입력')
#     print('2. 학생파일저장')
#     print('3. 학생파일읽기')
#     print('0. 프로그램종료')
#     print('-'*30)

#     choice= int(input('원하는 번호를 입력하세요.>> '))
    
#     if choice ==1:
        
#         if count==0:
#             print('학생성적입력을 선택하였습니다.')
#             print()
#             for i in range(3):
#                 stuNo=int(input('번호를 입력하세요.>> '))
#                 stuName=input('이름을 입력하세요.>> ')
#                 kor=int(input('국어점수를 입력하세요.>> '))
#                 eng=int(input('영어점수를 입력하세요.>> '))
#                 total=kor+eng
#                 avg=total/2
#                 student=[stuNo,stuName,kor,eng,total,avg]
#                 stuSave.append(student)
#                 print()
            
#         if count==1:
#             print('학생성적입력을 선택하였습니다.')
#             print()
#             stuNo=int(input('번호를 입력하세요.>> '))
#             stuName=input('이름을 입력하세요.>> ')
#             kor=int(input('국어점수를 입력하세요.>> '))
#             eng=int(input('영어점수를 입력하세요.>> '))
#             total=kor+eng
#             avg=total/2
#             student=[stuNo,stuName,kor,eng,total,avg]
#             stuSave.append(student)
#             print()
        
#         count=1
        
#     elif choice ==2:
#         print('학생파일저장을 선택하였습니다.')
#         print('학생성적이 파일에 저장되었습니다.')
#         print()
#         with open('학생성적프로그램.txt','w',encoding='utf8') as file:
#             for stu in stuSave:
#                 str1='{}\t{}\t{}\t{}\t{}\t{}\n'.format(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5])

#                 file.write(str1)

        
    
#     elif choice ==3:
#         print('학생파일읽기를 선택하였습니다.')
#         print()
#         print('번호\t이름\t국어\t영어\t합계\t평균')
#         print('-'*30)
#         with open('학생성적프로그램.txt','r',encoding='utf8') as file:
#             lines=file.readlines()
#             for line in lines:
#                 print(line,end='')
#             print()
    
#     elif choice==0:
#         print('프로그램이 종료되었습니다.')
#         break
    
#--------------

import json
data=[
    {'stuno':1,'stuname':'홍길동','kor':100,'eng':100,'total':200,'avg':100.0,'rank':0},
    "2,'이순신',100,100,200,100.0,0" # 딕셔너리로 저장하게 되면 type을 변경할 수 없어서 문자열형태로 바꿔야하는데 그러면 너무 복잡해짐
]

with open('2.txt','w',encoding='utf8') as file:
    file.write('{}'.format(data[0]))
    
with open('2.txt','r',encoding='utf8') as file:
    line=file.readline()
    print(type(dict(line)))
    print(dict(line))
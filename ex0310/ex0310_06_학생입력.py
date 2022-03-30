id='admin'
pw='1111'


# u_id=input('아이디를 입력하세요.>> ')
# u_pw=input('패스워드를 입력하세요.>> ')

# # 무한 반복
# while True:


#     if(id==u_id and pw==u_pw):
#         print('-'*60)
#         stu_no = input('학생번호를 입력하세요.>>') #omr카드: input을 의미함
#         stu_name=input('학생이름을 입력하시오.>>') #input으로 입력받는 것은 무조건 다 문자로 처리함
#         kor = int(input('국어점수를 입력하세요.>>'))
#         eng = int(input('영어점수를 입력하세요.>>'))
#         math = int(input('수학점수를 입력하세요.>>'))
#         total = kor+eng+math
#         avg= total/3
#         rank=0
#         student=[stu_no,stu_name,kor,eng,math,total,avg,rank]
#         students.append([student])
#         print(students)
#         # print('학생번호 : '+stu_no)
#         # print('학생이름 : '+stu_name)
#         # print('국어 :',kor)
#         # print('영어 :',eng)
#         # print('수학 :',math)
#         # print('합계 : {}'.format(total))
#         # print('평균 : {:.2f}'.format(avg))
#         print('-'*60)
#     else:
#         print('-'*60)
#         print('아이디, 패스워드가 일치하지 않습니다. 프로그램을 종료합니다.')
#         print('-'*60)
students=[]
count=1
# 무한 반복
while True:
    print('-'*60)
    stu_no = count #omr카드: input을 의미함
    print('학생번호: ', stu_no)
    stu_name=input('학생이름을 입력하시오.>> ') #input으로 입력받는 것은 무조건 다 문자로 처리함
    kor = int(input('국어점수를 입력하세요.>> '))
    eng = int(input('영어점수를 입력하세요.>> '))
    math = int(input('수학점수를 입력하세요.>> '))
    total = kor+eng+math
    avg= total/3
    rank=0
    student=[stu_no,stu_name,kor,eng,math,total,avg,rank]
    students.append(student)
    print(students)
    # print('학생번호 : '+stu_no)
    # print('학생이름 : '+stu_name)
    # print('국어 :',kor)
    # print('영어 :',eng)
    # print('수학 :',math)
    # print('합계 : {}'.format(total))
    # print('평균 : {:.2f}'.format(avg))
    print('-'*60)
    count+=1
    
    
# # 입력
# a= input()
# # 출력
# print(a)
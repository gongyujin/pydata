from stumanage.student import Student
import cx_Oracle



stuSave=[]

# 상단타이틀 출력
def topTitle():
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)

# 화면출력
def screenPrint():
    print('[ 학생성적프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생검색출력')
    print('4. 학생성적수정')
    print('5. 학생성적삭제')
    print('6. 학생등수처리')
    print('0. 프로그램종료')
    print()
    choice=int(input('원하는 번호를 입력하세요.>> '))

    return choice

# 학생성적입력
def stuInput():

    while True:
        print()
        print('[ 학생성적입력 ]')
        stuname = input('학생이름을 입력하세요. (0. 종료)>> ')
        if stuname=='0':
            break
        kor = int(input('국어점수를 입력하세요.>> '))
        eng = int(input('영어점수를 입력하세요.>> '))
        math = int(input('수학점수를 입력하세요.>> '))
        
        # oracle db에 저장
        conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe") # db연결 - sql developer 열림
        cs=conn.cursor() # 화면에 커서 클릭
        sql="insert into studata values(stu_seq.nextval,\
            :1,:2,:3,:4,:5,:6,:7)"
        cs.execute(sql,(stuname,kor,eng,math,(kor+eng+math),(kor+eng+math)/3,1)) # sql구문 입력
        print("insert : ",cs.rowcount)
        temp=Student(stuname, kor, eng)
        stuSave.append(temp)
        print('{}번. {} 학생이 저장되었습니다.'.format(temp.stuno,stuname))
    

# 학생전체출력
def stuoutput():
    print()
    topTitle()
    
    for stu in stuSave:
        print(stu)
    print()
    
# 학생검색출력
def stuSearch():
    print()
    print('[ 학생검색출력 ]')
    searchName=input('검색할 학생이름을 입력하세요.>> ')

    count=0
    for stu in stuSave:
        if stu==searchName:
            topTitle()
            print(stu)
            count=1
            break
    if count==0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')


# 학생성적수정
def stuModify():
    print()
    print('[ 학생성적수정 ]')
    searchName=input('수정할 학생이름을 입력하세요.>> ')

    count=0
    for stu in stuSave:
        if stu == searchName:
            print('{}의 학생이 검색되었습니다.'.format(searchName))
 
            print('[ 성적수정 ]')
            print('1. 국어점수 수정')
            print('2. 영어점수 수정')
            tempNum=int(input('수정과목 번호를 입력하세요.>> '))
            if tempNum==1:
                print('현재 국어점수 : {}'.format(stu.kor))
                score=int(input('수정할 국어점수를 입력하세요.>> '))
                stu.setKor(score)
                print('국어점수가 {}으로 변경되었습니다.'.format(score))

            elif tempNum==2:
                print('현재 영어점수 : {}'.format(stu.eng))
                score=int(input('수정할 영어점수를 입력하세요.>> '))
                stu.setEng(score)
                print('영어점수가 {}으로 변경되었습니다.'.format(score))
                    
            count=1
            break
            
    if count==0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')    
                
# 학생성적 삭제
def stuDelete():
    print()
    print('[ 학생성적삭제 ]')
    searchName=input('삭제할 학생이름을 입력하세요.>> ')
    for i, stu in enumerate(stuSave):
        if stu == searchName:
            print('{}의 학생이 검색되었습니다.'.format(searchName))
            flag=input('정말 삭제하시겠습니까? ')
            if flag == 'y' or flag == 'Y':
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(searchName))
                
            else:
                print('삭제가 취소되었습니다.')
            count=1
            break
        
    if count==0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')               
        
# 학생듣수 처리
def stuRank():
    print()
    for stu1 in stuSave:
        rankCount=1
        for stu2 in stuSave:
            if stu1<stu2: # 클래스 __lt__ 자동호출
                rankCount+=1
        stu1.rank=rankCount
        print('등수처리가 완료되었습니다.!')
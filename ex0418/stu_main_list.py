stuSave=[]
scount=0
def topTitle():
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)

def screenPrint():
    print('[ 학생성적프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('4. 학생성적수정')
    print('0. 프로그램종료')
    
    choice=int(input('원하는 번호를 입력하세요.>> '))
    
    return choice

# 학생성적입력
def stuInput():
    while True:
        global scount
        scount+=1
        print()
        print('[ 학생성적 입력 ]')
        stuname = input('학생이름을 입력하세요.(0. 종료)>> ')
        if stuname == '0':
            break
        
        kor= int(input('국어점수를 입력하세요.>> '))
        eng= int(input('영어점수를 입력하세요.>> '))
        math= int(input('수학점수를 입력하세요.>> '))
        student=[scount,stuname,kor,eng,math,kor+eng+math,(kor+eng+math)/3,1]
        stuSave.append(student)
        print('{}학생이 저장되었습니다.'.format(stuname))

# 학생성적전체출력
def stuOutput():
    print()
    topTitle()
    for stu in stuSave:
        print(stu)
        print(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7],sep='\t')  
    print()
                
# 학생성적수정
def stuModify():
    print()
    print('[ 학생성적수정 ]')
    searchName=input('수정할 학생이름을 입력하세요.>> ')
    
    count=0
    for i,stu in enumerate(stuSave):
        if stu[1] == searchName:
            print('{}의 학생이 검색되었습니다.'.format(searchName))
            
            print('[ 성적수정 ]')
            print('1. 국어점수 수정')
            print('2. 영어점수 수정')
            print('3. 수학점수 수정')
            tempNum=int(input('수정과목 번호를 입력하세요.>> '))
            if tempNum==1:
                print('현재 국어점수: {}'.format(stu[2]))
                score=int(input('수정할 국어점수를 입력하세요.>> '))
                stuSave[i][2]=score
                stuSave[i][5]=score+stu[3]+stu[4]
                stuSave[i][6]=(score+stu[3]+stu[4])/3
                print('국어점수가 {}으로 변경되었습니다.'.format(stu[2]))
            if tempNum==2:
                print('현재 영어점수: {}'.format(stu[3]))
                score=int(input('수정할 영어점수를 입력하세요.>> '))
                stuSave[i][3]=score
                stuSave[i][5]=score+stu[2]+stu[4]
                stuSave[i][6]=(score+stu[2]+stu[4])/3
                print('영어점수가 {}으로 변경되었습니다.'.format(stu[3]))
            if tempNum==3:
                print('현재 수학점수: {}'.format(stu[4]))
                score=int(input('수정할 수학점수를 입력하세요.>> '))
                stuSave[i][4]=score
                stuSave[i][5]=score+stu[2]+stu[3]
                stuSave[i][6]=(score+stu[2]+stu[3])/3
                print('수학점수가 {}으로 변경되었습니다.'.format(stu[4]))
            
            count=1
            break
    if count==0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.>> ')
           
  
while True:        
    choice=screenPrint()
    if choice==1:
        stuInput()
    elif choice==2:
        stuOutput()
    elif choice==4:
        stuModify()
    elif choice==0:
        break

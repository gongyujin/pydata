import cx_Oracle

def topTitle():
    print('번호','이름','국어','수학','영어','합계','평균','등수',sep='\t')
    print('-'*50)
    
def screenPrint():
    print()
    print('[ 학생성적처리프로그램 ]')
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생검색출력')
    print('4. 학생성적수정')
    print('5. 학생성적삭제')
    print('6. 학생등수처리')
    print('0. 프로그램종료')
    print('-'*30)
    choice=int(input('원하는 번호를 입력하세요.>> '))
    return choice

def stuInput():
    print()
    print('[ 학생성적입력 ] ')
    stuname=input('학생이름을 입력하세요.>> ')
    kor=int(input('국어점수를 입력하세요.>> '))
    eng=int(input('영어점수를 입력하세요.>> '))
    math=int(input('수학점수를 입력하세요.>> '))
    
    conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
    cs=conn.cursor()
    sql='insert into studata values(stu_seq.nextval,:1,:2,:3,:4,:5,:6,1)'
    cs.execute(sql,(stuname,kor,eng,math,(kor+eng+math),(kor+eng+math)/3))
    
    cs.close()
    conn.commit()
    conn.close()
    print('{}의 정보가 입력되었습니다.'.format(stuname))
    
def stuOutput():
    print()
    topTitle()
    conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
    cs=conn.cursor()
    sql='select * from studata'
    rows=cs.execute(sql)
    
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')
    
    sql='select count(*) from studata'
    cs.execute(sql)
    # cs.fetchall -> list타입, cs.fetchone은 한개만 가지고 옴
    count=cs.fetchone() 
    print('{}명의 데이터가 검색되었습니다.'.format(count[0]))

    cs.close()
    conn.close()
    
def stuSearch():
    print()
    print('[ 학생검색출력 ]')
    sname=input('검색할 학생이름을 입력하세요.>> ')
    
    conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
    cs=conn.cursor()
    sql='select * from studata'
    rows=cs.execute(sql)
    
    count=0
    for row in rows:
        if row[1] == sname:
            topTitle()
            print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')
            count=1
            break
    if count==0:
        print('검색한 학생이 없습니다. 다시 한번 입력하세요.')
        
    cs.close()
    conn.close()
    
def stuModify():
    print()
    print('[ 학생성적수정 ]')
    sname=input('수정할 학생이름을 입력하세요.>> ')
    
    conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
    cs=conn.cursor()
    sql='select * from studata'
    rows=cs.execute(sql)
    
    count=0
    for row in rows:
        if row[1]==sname:
            print('{} 학생이 검색되었습니다.'.format(sname))
            print('[ 성적 수정 ]')
            print('1. 국어점수 수정')
            print('2. 영어점수 수정')
            print('3. 수학점수 수정')
            
            tempNum=int(input('수정할 과목번호를 입력하세요.>> '))
            if tempNum==1:
                print('현재 국어점수 : {}'.format(row[2]))
                score=int(input('국어점수를 입력하세요.>> '))
                conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
                cs=conn.cursor()
                sql='update studata set kor=:1,total=:2,avg=:3 where stuno=:4'
                cs.execute(sql,(score,(score+row[3]+row[4]),(score+row[3]+row[4])/3,row[0]))
                cs.close()
                conn.commit()
                conn.close()
                print('{}으로 국어점수가 변경되었습니다.'.format(score))
            if tempNum==2:
                print('현재 영어점수 : {}'.format(row[3]))
                score=int(input('영어점수를 입력하세요.>> '))
                conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
                cs=conn.cursor()
                sql='update studata set eng=:1,total=:2,avg=:3 where stuno=:4'
                cs.execute(sql,(score,(score+row[2]+row[4]),(score+row[2]+row[4])/3,row[0]))
                cs.close()
                conn.commit()
                conn.close()
                print('{}으로 영어점수가 변경되었습니다.'.format(score))
            if tempNum==3:
                print('현재 수학점수 : {}'.format(row[4]))
                score=int(input('수학점수를 입력하세요.>> '))
                conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
                cs=conn.cursor()
                sql='update studata set math=:1,total=:2,avg=:3 where stuno=:4'
                cs.execute(sql,(score,(score+row[2]+row[3]),(score+row[2]+row[3])/3,row[0]))
                cs.close()
                conn.commit()
                conn.close()
                print('{}으로 수학점수가 변경되었습니다.'.format(score))
            
            count=1
            break
    if count==0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.')
        

def stuDelete():
    print()
    print('[ 학생성적삭제 ]')
    sname=input('삭제할 학생이름을 입력하세요.>> ')
    conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
    cs=conn.cursor()
    sql='select * from studata'
    rows=cs.execute(sql)
    
    count=0
    print('번호','이름',sep='\t')
    print('-'*20)
    for row in rows:
        if sname in row[1]:
            print(row[0],row[1],sep='\t')
            count=1
            
    if count==1:
        print('{} 학생이 검색되었습니다.'.format(sname))
        print()
        flag=input('삭제할 학생번호를 입력하세요. (0.삭제취소)>> ')
        if flag!='0':
            sql='delete studata where stuno='+flag
            cs.execute(sql)
            print('학생정보가 삭제되었습니다.')
        else:
            print('삭제가 취소되었습니다.')
    else:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.')
    
    cs.close()
    conn.commit()
    conn.close()
    
def stuRank():
    print()
    print('[ 학생등수처리 ]')
    conn=cx_Oracle.connect('ora_user/1234@localhost:1521/xe')
    cs=conn.cursor()
    sql='update studata a set rank=(select ranks from (select stuno,rank() \
        over(order by total desc) as ranks from studata) b where a.stuno=b.stuno)'
    
    cs.execute(sql)
    cs.close()
    conn.commit()
    conn.close()
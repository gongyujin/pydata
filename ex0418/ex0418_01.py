import cx_Oracle

# db 연결
conn=cx_Oracle.connect("ora_user/1234@localhost:1521/XE")
# db 실행후 저장공간 메모리 선언
cs=conn.cursor()
# sql구문 실행
rows = cs.execute("select * from studata")
print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
print('-'*60)
for row in rows:
    # print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t') 
    print(row) # 튜플형태로 찍힘 ==> 수정할수 없음

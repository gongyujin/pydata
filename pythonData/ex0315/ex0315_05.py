# 이름을 검색해서 삭제를 하는 프로그램을 만드시오.

# 찾는 사람 검색
# 찾는 사람 삭제
# 원하는 번호를 입력하세요.


students=[
    [1,'홍길동',100,100,200,100.0,0],
    [2,'이순신',100,100,200,100.0,0],
    [3,'유관순',100,100,200,100.0,0],
    [4,'김유신',100,100,200,100.0,0],
    [5,'김구',100,100,200,100.0,0]
]


while True:
    print('1. 찾는 사람 검색')
    print('2. 찾는 사람 삭제')
    choice=int(input('원하는 번호를 입력하세요.>> '))
    print()
    chk=0
    if choice==1:
        seName=input('찾고자 하는 학생이름을 입력하세요.>> ')
        
        for idx,stu in enumerate(students):
            if seName in stu:
                print(stu)
                chk=1
                # print(stu)
                print()
                break
        if chk==0:
            print('찾는 학생이 없습니다. 다시입력하세요.')
    
    elif choice==2: 
        seName=input('찾고자 하는 학생이름을 입력하세요.>> ')
        for idx,stu in enumerate(students):
            if seName in stu:
                del(students[idx])
                # break
                # 전체학생출력
                print(students)
                chk=1
                break
        if chk==0:
            print('찾는 학생이 없습니다. 다시입력하세요.')
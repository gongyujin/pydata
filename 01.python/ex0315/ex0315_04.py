students=[
    [1,'홍길동',100,100,200,100.0,0],
    [2,'이순신',100,100,200,100.0,0],
    [3,'유관순',100,100,200,100.0,0],
    [4,'김유신',100,100,200,100.0,0],
    [5,'김구',100,100,200,100.0,0]
]

while True:
    chkName=input('찾는 학생이름을 입력하세요.>> ')

    for idx, stu in enumerate(students):
        if chkName in stu:
            # 찾는 학생 삭제
            del(students[idx])
            # 출력
            # for s in stu:
            #     print(s,end=' ')
            # print()
            break
        # print(stu) #리스트
        # print()
    print(students)
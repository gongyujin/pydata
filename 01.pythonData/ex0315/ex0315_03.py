students=[
    [1,'홍길동',100,100,200,100.0,0],
    [2,'이순신',100,100,200,100.0,0],
    [3,'유관순',100,100,200,100.0,0],
    [4,'김유신',100,100,200,100.0,0],
    [5,'김구',100,100,200,100.0,0]
]
chkName = input('찾는 학생이름을 입력하세요.')
chk=0
# 5명의 학생을 검색
for stu in students:
    if stu[1] == chkName:
        print('[ 찾는 학생 성적 ]')
        # print('{} {} {} {} {} {} {}'.format(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6]))
        for s in stu:
            print(s,end=' ')
        print()
        chk=1
        break
    else:
        continue
    
if chk==0:  
    print('찾는 학생이 없습니다.')
    
    
# # 전체학생 성적을 출력
# for stu in students:
#     for s in stu:
#         print(s,end=' ')
#     print()

#-------------------------------
# del_Name=input('삭제하고자 하는 학생의 이름을 입력하세요.>> ')

    
# for i, stu in enumerate(students):
#     if stu[1] == del_Name:
#         del(students[i])
        
# print(students)

# aa=[10,20,30]
# # list에 데이터 추가
# aa.append(40)
# print(aa)
# # aa[4]=50 #없는 공간에 집어넣으면 에러가 남
# print(aa)

# # list데이터 변경
# aa[0]=[100] # 데이터 변경할때 list형으로 변경하면 숫자만 변경되는 것이 아니라 리스트형으로 변경됨
# print(aa)

# # list데이터 슬라이싱
# aa[1:2]=[200,300] #대입의 범위가 일치하지 않아도 모든 값을 추가적으로 삽입한다.
# print(aa)

# aa[1]=[1,2]
# print(aa)

# del(aa[1])
# print(aa)
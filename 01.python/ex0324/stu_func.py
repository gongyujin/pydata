import os
import json
import stu_class

stuSave=[] # 전역변수
sCount=0
count=0       # 학생검색 되었는지 체크하는 변수
# json읽기 함수
def jsonRead():
    global stuSave #global 선언하지 않아서 지역변수로 만들어버려서 error발생
    stuSave = json.load(open('stuData.json','r'))

# json저장 함수
def jsonSave():
    if 'stuData.json' in listdir():
        json.dump(stuSave,open('stuData.json','w'))
    else:
        json.dump(stuSave,open('stuData.json','w'))
        
# 학생번호 증가함수    
def stuCount():
    global sCount
    sCount=stuSave[-1]['stuno']+1   
    return sCount # global로 선언해서 변경된 값을 반환시킬 수 있음


# 화면출력함수
def screen_print():
    jsonRead()
    stuCount() # 호출해주지 않으면 0부터 나옴
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력') 
    print('2. 학생성적출력') 
    print('3. 학생성적수정')
    print('0. 프로그램종료')

    print('-'*25)
    # 숫자만 받는데, 문자를 입력하면 에러
    # 숫자만 받도록 변경
    choice = input('원하는 번호를 입력하세요.>> ')
    # isdigit() 숫자인지아닌지 확인함수
    if not choice.isdigit():  # 숫자
        print('숫자만 입력가능합니다.!!')
    return int(choice)

# 성적입력함수
def stu_input():
    global sCount
    # print('stu_input: ', sCount) # sCount는 여기 함수안에서 지역변수 이기 때문에 전역변수를 가져올 수 없음
    print('-- {}번째 학생등록 -- '.format(sCount))
    sName = input('학생이름을 입력하세요.>> ')
    kor = int(input('국어 점수를 입력하세요.>> '))
    eng = int(input('영어 점수를 입력하세요.>> ')) 
     
    stuSave.append(stu_class.Student(sCount,sName,kor,eng))
    print(stuSave)
    jsonSave()  # json저장함수 호출
    sCount += 1 #학생인원 count 1증가
    print('학생성적이 저장되었습니다.')
    return sCount

# 학생전체 출력        
def stu_print():
    jsonRead()
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)
    # [[1,홍길동,100,100,200,100.0,0]]
    for stu in stuSave:
        # print정렬
        print(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],\
            stu['total'],stu['avg'],stu['rank'],sep='\t')
        # for k,v in stu.items():
        #    print('{}\t'.format(v),end='') 
            # print() #줄바꿈
            
#화면 출력 구성
#1. 학생성적입력
#2. 학생성적수정
# ....
#프로그램을 무한 반복
#학생성적입력 부분을 구성



# stuSave=[[0]*7 for _ in range(10)]

# stuCount=0
# while True:
#     print('-'*25)
#     print('[ 학생성적 프로그램 ]')
#     print('-'*25)
#     print('1. 학생성적입력')
#     print('2. 학생성적수정')
#     print('3. 학생성적삭제')
#     print('0. 프로그램 종료')
#     print('')
#     choice=int(input('원하는 번호를 입력하세요.>> '))    
#     if choice==1:
        
#         print('학생성적 입력을 선택하였습니다.')
#         print('-- {}번째 학생등록 --'.format(stuCount+1))
#         stuName=input('학생이름을 입력하세요.>> ')
#         kor=int(input('국어점수를 입력하세요.>> '))
#         eng=int(input('영어점수를 입력하세요.>> '))
#         total=kor+eng
#         avg=total/2
        
#         stuSave[stuCount][0]=stuCount+1
#         stuSave[stuCount][1]=stuName
#         stuSave[stuCount][2]=kor
#         stuSave[stuCount][3]=eng
#         stuSave[stuCount][4]=total
#         stuSave[stuCount][5]=avg
        
#         stuCount+=1
#         print('학생성적이 저장되었습니다.')
#         print(stuSave)
        
#     elif choice==2:
#         print('학생성적 수정을 선택하였습니다.')
        
#     elif choice==3:
#         print('학생성적 삭제를 선택하였습니다.')
    
#     elif choice==0:
#         print('프로그램을 종료합니다.')
#         break
    
    
from re import search


stuSave=[] #데이터 최종저장리스트
stuCount=0
while True:
    print('-'*60)
    print('[ 학생성적 프로그램 ]')
    print('-'*60)
    print('1. 학생성적입력') #완료
    print('2. 학생성적수정') 
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력') #완료
    print('5. 학생검색출력') #완료
    print('6. 등수처리')
    print('0. 프로그램종료') #완료
    print(''*60)
    
    #숫자만 받는데, 문자를 입력하면 에러 ==> 숫자만 받도록 변경
    choice=input('원하는 번호를 입력하세요.>> ')
    print()
    if not choice.isdigit(): # 숫자인지 아닌지 확인 함수
        print('숫자만 입력가능합니다.!!!')
        continue
    choice=int(choice) #int형으로 변경
    
    # if choice=='1' or choice=='2' or choice=='3' or choice=='4'or choice=='5'or choice=='6' or choice=='0':
    #     choice=int(choice)
    # else:
    #     print('잘못된 입력 번호입니다. 번호를 다시 입력해주세요. >>')
        
    
    
    if choice==1:
        
        print('학생성적 입력을 선택하였습니다.')
        print('-- {}번째 학생등록 --'.format(stuCount+1))
        stuName=input('학생이름을 입력하세요.>> ')
        kor=int(input('국어점수를 입력하세요.>> '))
        eng=int(input('영어점수를 입력하세요.>> '))
        total=kor+eng
        avg=total/2
        rank=0
        
        # student=[re_Count,re_Name,re_kor,re_eng,re_kor+re_eng,(re_kor+re_eng)/2,rank]
        # 튜플 형태로 바꿈 => json형태로 바뀐것
        student={'stuno':stuCount+1,'stuname':stuName, 'kor':kor,'eng':eng,'total':total,'avg':avg,'rank':rank}
        stuSave.append(student)
        stuCount+=1
        
        print('학생성적이 저장되었습니다.')
        
    elif choice==2:
        print('학생성적 수정을 선택하였습니다.')
        print('-'*50)
        print('[ 학생성적 수정페이지 ]')
        print('-'*50)
        re_Name=input('수정할 학생이름을 입력하세요.>> ')
        
        count=0 # 학생이름검색이 되었는지 확인하는 변수
        for i, stu in enumerate(stuSave):
            if re_Name in stu.values(): 
                print('{} 학생이 검색되었습니다.'.format(re_Name))
                print()
                #1. 이름수정   --> 여기서 '이름'은 유일코드여서 수정할 수 없음 (primary key)
                #1. 국어점수 수정
                #2. 영어점수 수정
                print('[점수 수정]')
                print('-'*50)
                print('1. 국어점수 수정')
                print('2. 영어점수 수정')
                print('0. 상위메뉴 이동')
                
                searchNo=input('수정할 과목 번호를 입력하세요.>> ')
                if not searchNo.isdigit(): # 숫자인지 아닌지 확인 함수
                    print('숫자만 입력가능합니다.!!!')
                    continue
                searchNo=int(searchNo) #int형으로 변경
                
                if searchNo ==1: # 국어점수 수정
                    print('현재 국어점수 :', stu['kor'])
                    score = int(input('변경할 국어점수를 입력하세요.>> '))
                    stu['kor'] =score # 주소값이 복사된 것이기 때문에 임시변수여도 최종변수에서 변경을 하지 않아도 알아서 변경됨
                    
                    # 합계, 평균 점수 변경
                    stu['total']=stu['kor']+stu['eng']
                    stu['avg']=stu['total']/2
                                        
                    print('국어점수가 변경되었습니다.!!')
                elif searchNo ==2: # 영어점수 수정
                    pass
                
                
                elif searchNo ==0:
                    print('상위메뉴로 돌아갔습니다.')
                count=1 #학생검색이 됨.
                break
        
        if count==0:
            print('{} 학생이 없습니다.'.format(re_Name))
        
        
        
        # for i in range(len(stuSave)):
        #     if stuSave[i][1]==re_Name:
        #         re_Count=stuSave[i][0]
        #         re_kor=int(input('국어점수를 입력하세요.>> '))
        #         re_eng=int(input('영어점수를 입력하세요.>> '))
        #         rank=0
        #         student=[re_Count,re_Name,re_kor,re_eng,re_kor+re_eng,(re_kor+re_eng)/2,rank]
        #         stuSave[i]=student
            
        
    elif choice==3:
        print('학생성적 삭제를 선택하였습니다.')
        del_Name=input('삭제할 학생이름을 입력하세요.>> ')
        
        count=0
        for i, stu in enumerate(stuSave):
            if del_Name in stu.values(): 
                print('{}이 있습니다.'.format(del_Name))
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(del_Name))
                count=1
                break
        
        if count==0:
            print('{} 학생이 없습니다.'.format(del_Name))
        
        
        
        # chk=0
        # for i, stu in enumerate(stuSave):
        #     if del_Name in stu:
        #         del(stuSave[i])
        #         chk=1
        #         break
        #     else:
        #         continue
                
        # if chk==0:
        #     print('찾고자 하는 학생이 없습니다.')
                
    elif choice==4:
        print('학생성적 전체출력을 선택하였습니다.')
        
        print('번호', '이름', '국어', '영어', '합계', '평균', '등수', sep='\t')
        print('-'*60)
        for stu in stuSave: # stu는 리스트가 아닌 딕셔너리
            for k,v in stu.items(): # i는 key값
                print('{}\t'.format(v),end='')
            print()
        # for i in range(len(stuSave)):
        #     print('학생이름: {}, 국어점수: {}, 영어점수: {}, 합계: {}, 평균: {}, 등수: {}'.format(stuSave[i][1],stuSave[i][2],stuSave[i][3],stuSave[i][4],stuSave[i][5],stuSave[i][6]))
    
    elif choice==5:
        print('학생검색 출력을 선택하였습니다.')
        se_Name=input('검색하고 싶은 학생이름을 입력하세요.>> ')
        print('번호\t이름\t국어\t영어\t합계\t평균\t등수')
        print('-'*60)
        for stu in stuSave:
            if stu[1]==se_Name:
                for i in stu.values():
                    print('{}\t'.format(str(i)),end='')
        print()
            
        # for i in range(len(stuSave)):
        #     if stuSave[i][1]==se_Name:
        #         print('{}\t'.format(str(stuSave[i])),end='')
                
    elif choice==6:
        print('등수처리를 선택하였습니다.')
        
    elif choice==0:
        print('프로그램을 종료합니다.')
        break
    
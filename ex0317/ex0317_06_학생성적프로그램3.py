count=1
stuSave=[]
while True:
    print('-'*60)
    print('[ 학생성적 프로그램 ]')
    print('-'*60)
    print('1. 학생성적입력') # 완료
    print('2. 학생성적수정') # 완료
    print('3. 학생성적삭제') # 완료
    print('4. 학생성적전체출력') # 완료
    print('5. 학생검색출력') # 완료
    print('6. 등수처리')
    print('0. 프로그램종료') # 완료
    print('-'*60)

    choice=input('원하는 번호를 입력하세요.>> ')
    
    if not choice.isdigit():
        print('번호를 다시 입력하세요.')
        continue
    choice=int(choice)
    
    if choice==1:
        print('학생성적 입력을 선택하였습니다.')
        print()
        stuNo=count
        print('-'*30)
        print('-- {}번째 학생등록 --'.format(stuNo))
        print('-'*30)
        stuName=input('학생이름을 입력하세요.>> ')
        kor=int(input('국어점수를 입력하세요.>> '))
        eng=int(input('영어점수를 입력하세요.>> '))
        print('-'*60)
        student={'번호':stuNo,'이름':stuName,'kor':kor,'eng':eng,'total':kor+eng,'avg':(kor+eng)/2,'rank':0}        
        stuSave.append(student)    
        count+=1

        print('학생성적이 저장되었습니다.')
        
    elif choice==2:
        print('학생성적 수정을 선택하였습니다.')
        print('-'*50)
        print('[ 학생성적 수정페이지 ]')
        print('-'*50)
        
        count=0
        searchName=input('수정할 학생이름을 입력하세요.>> ')
        for i,stu in enumerate(stuSave):
            if searchName in stu.values(): #stu는 딕셔너리, value만 뽑아오기
                print('{} 학생이 검색되었습니다'.format(searchName))
                print('-'*50)
                print('[점수 수정]')
                print('-'*50)
                print('1. 국어점수 수정')
                print('2. 영어점수 수정')
                print('0. 상위메뉴 이동')
                print('-'*50)
                input1=input('수정할 과목 번호를 입력하세요.>> ')
                
                if not input1.isdigit():
                    print('번호를 다시 입력하세요.')
                    continue
                input1=int(input1)
                
                if input1==1:
                    print('현재 국어점수:',stu['kor'])
                    score=int(input('변경할 국어점수를 입력하세요.>> '))
                    stu['kor']=score
                    
                    stu['total'] =stu['kor']+stu['eng']
                    stu['avg']=stu['total']/2
                    
                    print('국어점수가 변경되었습니다.!!')
                
                elif input1==2:
                    print('현재 영어점수:',stu['eng'])
                    score=int(input('변경할 영어점수를 입력하세요.>> '))
                    stu['eng']=score
                    
                    stu['total'] =stu['kor']+stu['eng']
                    stu['avg']=stu['total']/2
                    
                    print('영어점수가 변경되었습니다.!!')
                elif input1==0:
                    print('상위메뉴로 돌아갑니다.')
                    
                count=1    
                break
                
                
        if count==0:
            print('{} 학생이 존재하지 않습니다.'.format(searchName))
        
    elif choice==3:
        print('학생성적 삭제를 선택하였습니다.')
        count=0
        searchName=input('삭제할 학생이름을 입력하세요.>> ')
        for i, stu in enumerate(stuSave):
            if searchName in stu.values():
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(searchName))
                count=1
                break
        
        if count==0:
            print('{} 학생이 존재하지 않습니다.'.format(searchName))
    elif choice==4:
        print('학생성적 전체출력을 선택하였습니다.')
        print()
        print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
        print('-'*60)
        for stu in stuSave: #stuSave는 리스트
            for k,v in stu.items(): #stu는 딕셔너리 --> items를 이용하여 튜플로 만들어줌
                print('{}\t'.format(v),end='')
            # 탭 길이 맞추고 싶을때
            # print(stu['번호'],stu['이름'],stu['kor'],stu['eng'],stu['total'],stu['avg'],stu['rank'],sep='\t')    
            print()           
    
    elif choice==5:
        print('학생성적 검색을 선택하였습니다.')
        print()
        count=0
        searchName=input('검색할 학생이름을 입력하세요.>> ')
        
        for i, stu in enumerate(stuSave):
            if searchName in stu.values():
                print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
                print('-'*60)
                print(stu['번호'],stu['이름'],stu['kor'],stu['eng'],stu['total'],stu['avg'],stu['rank'],sep='\t')    
                count=1
                break
        
        if count==0:
            print('{} 학생이 존재하지 않습니다.'.format(searchName))
            
        # print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
        # print('-'*60)
        # for stu in stuSave: # stu는 딕셔너리
        #     if stu['이름']==searchName:
        #         for i in stu.values():
        #             print('{}\t'.format(str(i)),end='')
        #     print()
    
    elif choice==6:
        for stu in stuSave:
            rcount=1
            for stu2 in stuSave:
                if stu['total'] < stu2['total']: # total 점수 비교
                    rcount+=1 # stu2가 더 클 경우에만 1증가
            stu['rank']=rcount # 등수입력
            
        print('등수처리가 완료되었습니다.')
         
    elif choice==0:
        print('프로그램을 종료합니다.')
        break
stu1={
    'id':'aaa','pass':'1111','name':'홍길동','tel':'010-0000-0000',
    'address':'서울','gender':'male','hobby':'game'  
}


# 1. 키값 검색
# 2. value값 검색
# 3. 딕셔너리 전체 출력
# 원하는 번호를 입력하세요.>> 


# 프로그램을 구성하시오.

# 무한반복
while True:
    print('[ 딕셔너리 확인 프로그램 ]')
    print('1. 키값 검색')
    print('2. value값 검색')
    print('3. 딕셔너리 전체출력')
    print('4. 프로그램 종료')
    print()
    choice=input('원하는 번호를 입력하세요.>> ')
    
    if not choice.isdigit():
        print('숫자만 입력가능합니다.!!')
        continue
    
    choice=int(choice)
    
    if choice ==1:
        while True:
            # 키값 검색
            key_search=input('키값을 입력하세요. (0: 상위메뉴 이동)>> ')
            
            if key_search.isdigit():
                if int(key_search)==0:
                    print('상위메뉴로 돌아갑니다.')
                    break
            
            if key_search in stu1:
                print('{} : {} 값이 있습니다.'.format(key_search,stu1[key_search]))
                print('입력하신 키값이 있습니다.')
            # elif key_search=='0':
            #     break
            else:
                print('{}의 key값은 없습니다.'.format(key_search))
            print()
            
    elif choice ==2:
        while True:
            # value값 검색
            value_search=input('value값을 입력하세요. (0: 상위메뉴 이동)>> ')
            
            if value_search.isdigit():
                    if int(value_search)==0:
                        print('상위메뉴로 돌아갑니다.')
                        break 
            
            chk=0
            for key in stu1:
                if stu1[key]==value_search:
                    print('{} : {} 값이 있습니다.'.format(key,stu1[key]))
                    chk=1
                    break
            if chk==0:
                print('{}의 value값은 없습니다.'.format(value_search))
            print()
    
    elif choice==3:
        for key in stu1:
            print('{:7s} : {}'.format(key,stu1[key]))
        print()
        
    elif choice==4:
        print('프로그램을 종료합니다.')
        break
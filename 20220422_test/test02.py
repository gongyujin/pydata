def screenPrint(): # 메인페이지 출력 함수
    print('[ 자판기 프로그램 ]')
    print('1. 금액충전')
    print('2. 아메리카노(Hot) 2000원')
    print('3. 아메리카노(Ice) 2500원')
    print('4. 카페라떼 4000원')
    print('5. 주문조회')
    print('0. 프로그램종료')
    print('-'*30)
    choice=int(input('원하는 번호를 입력하세요.>> '))
    return choice

def payPrint(): # 메뉴선택시 페이지 출력 함수
    print()
    print('1. 결제')
    print('2. 계속주문')
    print('3. 주문취소')
    print('-'*30)
    pbutton=int(input('원하는 번호를 입력하세요.>> '))
    return pbutton

def mcharge(): # 금액충전함수
    print()
    print('금액충전이 선택되었습니다.')
    money= int(input('충전할 금액을 입력하세요.>> '))
    mstore[3]+=money
    print('{}원 금액이 충전되었습니다.'.format(money))
    
def moutput(): # 전체주문 조회
    print()
    print('[ 주문조회 ]')
    print('아메리카노(Hot)','아메리카노(Ice)','카페라떼','잔액',sep='\t')
    print('-'*60)
    print(mstore[0],mstore[1],mstore[2],mstore[3],sep='\t\t')

def morder(menu,choice,money1): # 결제
    global keep
    global mstore
    print()
    count=0
    if mstore[3]-keep[3] < money1:
        print('충전금액이 부족합니다.')
        print()
        print('1. 금액충전이동')
        print('2. 주문취소')
        print('-'*30)
        tempNum=int(input('결제 부족시 금액을 충전해주세요. 금액을 충전하시겠습니까?>> '))
        if tempNum==1:
            mcharge()
            print('다시 주문해주세요.')
            count=1
        elif tempNum==2:
            print('주문이 취소되었습니다.')
            count=1
    
    if count==0:
            mstore[0]+=keep[0]
            mstore[1]+=keep[1]
            mstore[2]+=keep[2]
            mstore[choice-2]+=1
            mstore[3]-=money1
            mstore[3]-=keep[3]
            print(menu+'주문완료 현재 잔액 : ',mstore[3])
            print('주문이 완료되었습니다.')
            
    keep=[0,0,0,0] # 장바구니 초기화



# [아메리카노(hot) 개수,아메리카노(ice) 개수,카페라떼 개수,충전금액]
mstore=[0,0,0,0] 
keep=[0,0,0,0] # 장바구니에 있는 hot개수, ice개수, 카페라떼 개수, 미결제금액
while True:
    print()
    choice=screenPrint() # 메인화면 호출
    if choice ==1:
        mcharge() # 금액충전 호출
        
    elif choice==2: #아메리카노 핫
        pbutton=payPrint() # 결제화면 호출
        if pbutton==1: # 결제 
            morder('아메리카노(Hot)',choice,2000)
        elif pbutton==2:
            keep[choice-2]+=1 # 장바구니 개수
            keep[3]+=2000 # 미결제 금액
            continue
        elif pbutton==3:
            keep=[0,0,0,0] # 장바구니 초기화
            print('주문이 취소되었습니다.')
    elif choice==3: #아메리카노 아이스
        pbutton=payPrint() # 결제화면 호출
        if pbutton==1: # 결제 
            morder('아메리카노(Ice)',choice,2500)
        elif pbutton==2:
            keep[choice-2]+=1 # 장바구니 개수
            keep[3]+=2500 # 미결제 금액
            continue
        elif pbutton==3:
            keep=[0,0,0,0] # 장바구니 초기화
            print('주문이 취소되었습니다.')
    elif choice==4: #카페라떼
        pbutton=payPrint() # 결제화면 호출
        if pbutton==1: # 결제 
            morder('카페라떼',choice,4000)
        elif pbutton==2:
            keep[choice-2]+=1 # 장바구니 개수
            keep[3]+=4000 # 미결제 금액
            continue
        elif pbutton==3:
            keep=[0,0,0,0] # 장바구니 초기화
            print('주문이 취소되었습니다.')

    elif choice==5:
        moutput()
    elif choice==0:
        print('프로그램을 종료합니다.')
        break
                    
                    
                
                
                
        
        
from stumanage.lottodef import *
# 10개 :입력번호
# 1~10개 구매할 수 있음.

# 로또번호에 몇개 맞았는지 출력하시오.
# 1등-6개: 10억, 2등-5개:1억, 3등-4개: 1000만원, 4등-3개: 100만원, 5등-2개: 1만원

# [1번째 로또]
# 로또당첨번호 : 1,2,3,4,5,6 # 로또당첨번호는 같음
# 로또입력번호 : 4,5,6,7,8,9
# 당첨확인번호 : 4,5,6 (3개)
# 당첨금액 : 100만원

# [2번째 로또]
# 로또당첨번호 : 1,2,3,4,5,6
# 로또입력번호 : 4,5,6,7,8,9
# 당첨확인번호 : 4,5,6 (3개)
# 당첨금액 : 100만원


# 로또담청번호 생성
lottoNum()
# 로또입력번호 생성
buynum=myNum()
# 당첨번호 맞추기
okNum()

score=['10억','1억','1000만원','100만원','1만원','꽝','꽝']

for i in range(buynum):    
    print('[{}번째 로또]'.format(i+1))
    print('로또당첨번호 : ',end='')
    for num in lotto:
        print(num,end=' ')
    print()
    print('로또입력번호 : ',end='')
    for mynum in mynumList[i]:
        print(mynum,end=' ')
    print()
    print('당첨확인번호: ', end='')
    for oknum in oknumList[i]:
        print(oknum,end=' ')
    print('({}개)'.format(len(oknumList[i])))
    print('당첨금액 :',score[6-len(oknumList[i])])
    print()
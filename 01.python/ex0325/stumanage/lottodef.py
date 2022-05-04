from random import *
# 로또담청번호 생성
lotto=[]
def lottoNum():
    lottonum=[i for i in range(1,46)]
    for i in range(500):
        rno=randint(0, 44)
        lottonum[0],lottonum[rno]=lottonum[rno],lottonum[0]
    lotto=lottonum[:6]

# 로또입력번호 생성
mynumList=[]

def myNum():
    count=1

    buynum=int(input('몇개의 로또를 구매하시겠습니까? '))
    while count<buynum+1:
        mynum=[]
        print('[{}번째 로또]'.format(count))
        for i in range(6):
            num=int(input('{}번째 로또 번호를 입력하세요.>> '.format(i+1)))
            mynum.append(num)
        print()
        mynumList.append(mynum)
        count+=1
    return buynum
        
# 당첨번호 맞추기
oknumList=[]
def okNum():
    for mynum in mynumList:
        oknum=[]
        for num in mynum:
            if num in lotto:
                oknum.append(num)
        oknumList.append(oknum)


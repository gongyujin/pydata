import lotto # import로 파일하나로 합치면 됨

# ---------------프로그램 시작---------------
lottoNum=[]
lotto6=[]
lottoInput=[]
okNum=[]
count=0

# 복사되어서 변경된 데이터값을 불러옴
lotto.lottoProduce(lottoNum) # 로또번호생성 
lotto.lottosuffle(lottoNum, lotto6) # 로또섞기
print(lotto6)
lotto.inputNo(lottoInput) # 로또번호입력
lotto.lottoOk(okNum, lotto6, lottoInput,count)
count=lotto.lottoOk(okNum, lotto6, lottoInput,count)
# 맞춘 번호가 몇개인지, 번호가 어떤 것인지 찾는 함수만들기
print(lottoNum)
print('당첨번호 :', lotto6)
print('입력번호 :', lottoInput)
print('맞춘개수 :', count)
print('맞춘번호 :', okNum)
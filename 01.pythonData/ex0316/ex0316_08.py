from random import *

words1={
    '자동차':'car',
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '사자':'lion',
    '직업':'job',
    '사과':'apple',
    '여우':'fox'
}

# 랜덤으로 5개를 뽑는다.
level1=list(words1.keys())


randTemp=[]
count=0
while count<5:
    rno = randint(0,9)
    if not level1[rno] in randTemp:
        randTemp.append(level1[rno])
    else:
        continue
    count+=1
print(randTemp)




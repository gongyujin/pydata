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

words2={
    '연필':'pencil',
    '자':'ruler',
    '책':'book',
    '양말':'sock',
    '모자':'hat',
    '개':'dog',
    '잠':'sleep',
    '먹다':'eat',
    '읽다':'read',
    '피아노':'piano'
}

# totallist=[키] words1 5개, words2 5개 랜덤으로 담아보시오.
# totallist 10개가 담긴 리스트를 출력하시오.

# tdic = {key:value} 10개를 출력하시오.
# 예) words1 3개, words2 7개로 구성하여 만들기

# # 강사님이 해주신 코드
# ww=list(words1.keys())
# www=list(words1.values())
# wlist=list(words1.items()) #타입: 리스트

# count=0
# listtemp=[] # 임시저장
# while count<5:
#     rno=randint(0,9)
#     # 랜덤으로 리스트에 담기
#     if not wlist[rno] in listtemp:
#         listtemp.append(wlist[rno])
#         count+=1
#     else:
#         continue
    
# 튜플로 만들기
level1=list(words1.items())
level2=list(words2.items())

randTamp1=[]
randTamp2=[]
count1=0
while count1<5:
    rno=randint(0,9)
    if not level1[rno] in randTamp1:
        randTamp1.append(level1[rno])
        randTamp2.append(level2[rno])
        count1+=1
    else:
        continue

list=[]
for i in range(5):
    list.append(randTamp1[i])
    list.append(randTamp2[i])

tdic=dict(list)
totallist=[]
for key in tdic:
    totallist.append(key)
print(totallist)
print(tdic)


# ----------- 리스트로 먼저 만들고 딕셔너리로 바꾸기------------------   
# level1=list(words1.keys())
# level2=list(words2.keys())

# randTamp1=[]
# randTamp2=[]
# count1=0
# while count1<5:
#     rno=randint(0,9)
#     if not level1[rno] in randTamp1:
#         randTamp1.append(level1[rno])
#     else:
#         continue
#     count1+=1
# count1=0
# while count1<5:
#     rno=randint(0,9)
#     if not level2[rno] in randTamp2:
#         randTamp2.append(level2[rno])
#     else:
#         continue
#     count1+=1
    
# totallist=[]
# for i in range(5):
#     totallist.append(randTamp1[i])
#     totallist.append(randTamp2[i])
    
# print(totallist)

# #-------------------------------------------------
# tdic={}

# for word1 in totallist:
#     if word1 in words1:
#         tdic[word1]=words1[word1]
        
# for word2 in totallist:
#     if word2 in words2:
#         tdic[word2]=words2[word2]
    
# print(tdic)

#-----------------------------------------------------------
input1=int(input('words1에서 원하는 개수를 입력하세요.>> '))
input2=int(input('words2에서 원하는 개수를 입력하세요.>> '))

randTamp1=[]
randTamp2=[]
count1=0
while count1<input1:
    rno=randint(0,9)
    if not level1[rno] in randTamp1:
        randTamp1.append(level1[rno])
        count1+=1
    else:
        continue

count1=0
while count1<input2:
    rno=randint(0,9)
    if not level2[rno] in randTamp2:
        randTamp2.append(level2[rno])
        count1+=1
    else:
        continue
    

totallist=[]
for i in range(input1):
    totallist.append(randTamp1[i])
    
for i in range(input2):
    totallist.append(randTamp2[i])

tdic=dict(totallist)
list=[]
for key in tdic:
    list.append(key)
print(list)
print(tdic)
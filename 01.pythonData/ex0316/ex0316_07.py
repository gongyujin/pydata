words1={
    '자동차':'car',
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '사자':'lion',
    '직업':'job',
    '사과':'apple'
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

# ok_count=0
# not_count=0
# corr={}
# for word in words:
#     inwds=input('{}의 영어단어를 입력하세요. (0: 프로그램 종료)>> '.format(word))
#     if inwds.isdigit():
#         if int(inwds)==0:
#             print('프로그램 종료')
#             break
    
#     if words[word]==inwds:
#         print('정답입니다. {} : {}'.format(word,words[word]))
#         ok_count+=1
#         corr[inwds]='정답'
    
#     else:
#         print('오답입니다. {} : {}'.format(word,words[word]))
#         not_count+=1
#         corr[inwds]='오답'
#     print()


# print('[ 정답확인 ]')
# print('-'*50)

# # 오답노트: 내가 입력한거 맞다 아니다 출력하기
# for i,key in enumerate(corr):
#     print('{}. {}'.format(i+1,corr[key]))
#     if corr[key] =='오답':
#         print('{}. {}'.format(i+1,corr[key]), '입력한 답: {}'.format(key))
        
# # 정답: 9 오답: 1 90점
# print('정답: {} 오답: {} {}점'.format(ok_count,not_count,10*ok_count))
# print()

print('[ 영어 단어 테스트 ]')
print('1. 초등1-2학년')
print('2. 초등3-4학년')
print('-'*50)
inword=int(input('난이도를 선택하세요.>> '))    

#난이도 선택
if inword==1:
    level=words1
    print('1번 문항을 선택하였습니다.')
    print()
elif inword==2:
    level=words2
    print('2번 문항을 선택하였습니다.')
    print()
    

wordlist=[]
for word in level:
    inwds=input('{}의 영어단어를 입력하세요. (0: 프로그램 종료)>> '.format(word))
    if inwds.isdigit():
        if int(inwds)==0:
            print('프로그램 종료')
            break
    
    if level[word]==inwds:
        print('정답입니다. {} : {}'.format(word,level[word]))
        # [입력한 value, 정답, key, key에 대한 value값]
        wlist=[inwds,'O',word,level[word]]
        wordlist.append(wlist)
    else:
        print('오답입니다. {} : {}'.format(word,level[word]))
        wlist=[inwds,'X',word,level[word]]
        wordlist.append(wlist)
        
        
    print()



ocount,xcount=0,0 #정답, 오답 개수
# 정답, 오답 출력
print('[ 정답확인 ]')
print('-'*50)
for idx, wlist in enumerate(wordlist):
    if 'O' in wlist:
        ocount+=1
        # 1. 정답
        # 2. 오답
        print('{:2d}. {}, {:4s} : {:7s}'.format(idx+1,'정답',wlist[2],wlist[0]))
    else:
        xcount+=1
        print('{:2d}. {}, {:4s} : {:7s}, 입력값 :{}'.format(idx+1,'오답',wlist[2],wlist[3],wlist[0]))

# 최종점수
print('정답: {}, 오답: {}, 점수: {}'.format(ocount,xcount,ocount*10))
import json
data=[
    {'stuno':1,'stuname':'홍길동','kor':100,'eng':100,'total':200,'avg':100.0,'rank':0},
    {'stuno':2,'stuname':'이순신','kor':100,'eng':100,'total':200,'avg':100.0,'rank':0},
    {'stuno':3,'stuname':'유관순','kor':100,'eng':100,'total':200,'avg':100.0,'rank':0},
    {'stuno':4,'stuname':'김구','kor':100,'eng':100,'total':200,'avg':100.0,'rank':0}
]


#json파일 저장함수
json.dump(data,open('2.json','w',encoding='utf-8'))

#json파일 읽어오기
data2 = json.load(open('2.json',encoding='utf-8')) # json이 자동으로 파싱해주기 때문에 리스트안에 딕셔너리가 살아있음
print(data2)
print(type(data2))

#----------------------------------------------------------------------------
stuSave=[]
count=0
while True:
    print('[ 학생성적프로그램 ]')
    print('1. 학생성적입력')
    print('2. 학생파일저장')
    print('3. 학생파일읽기')
    print('0. 프로그램종료')
    print('-'*30)

    choice= int(input('원하는 번호를 입력하세요.>> '))
    
    if choice ==1:
        
        if count==0:
            print('학생성적입력을 선택하였습니다.')
            print()
            for i in range(3):
                stuNo=int(input('번호를 입력하세요.>> '))
                stuName=input('이름을 입력하세요.>> ')
                kor=int(input('국어점수를 입력하세요.>> '))
                eng=int(input('영어점수를 입력하세요.>> '))
                total=kor+eng
                avg=total/2
                student={'stuno':stuNo,'stuname':stuName,'kor':kor,'eng':eng,'total':total,'avg':avg,'rank':0}
                stuSave.append(student)
                print()
            
        if count==1:
            print('학생성적입력을 선택하였습니다.')
            print()
            stuNo=int(input('번호를 입력하세요.>> '))
            stuName=input('이름을 입력하세요.>> ')
            kor=int(input('국어점수를 입력하세요.>> '))
            eng=int(input('영어점수를 입력하세요.>> '))
            total=kor+eng
            avg=total/2
            student={'stuno':stuNo,'stuname':stuName,'kor':kor,'eng':eng,'total':total,'avg':avg,'rank':0}
            stuSave.append(student)
            print()
        
        count=1
        
    elif choice ==2:
        print('학생파일저장을 선택하였습니다.')
        print('학생성적이 파일에 저장되었습니다.')
        print()
        json.dump(stuSave,open('stuData.json','w'))

        
    
    elif choice ==3:
        print('학생파일읽기를 선택하였습니다.')
        print()
        print('번호\t이름\t국어\t영어\t합계\t평균')
        datas=json.load(open('stuData.json')) # json이 자동으로 파싱해주기 때문에 리스트안에 딕셔너리가 살아있음
        for data in datas:
            for k,v in data.items():
                print('{}\t'.format(v),end='')
            print()
        print()
        
        # print('-'*30)
        # with open('학생성적프로그램.txt','r',encoding='utf8') as file:
        #     lines=file.readlines()
        #     for line in lines:
        #         print(line,end='')
        #     print()
    
    elif choice==0:
        print('프로그램이 종료되었습니다.')
        break
    
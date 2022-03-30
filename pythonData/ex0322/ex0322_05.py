import os

# # 파일쓰기
# with open('1.txt','w',encoding='utf8') as file:
#     file.write('aaa')

# # 파일내용추가
# with open('1.txt','a',encoding='utf8') as file:
#     file.write('6\t김유신\t100\t100\t200\t100.0\t0\n')  

# # 파일읽어오기
# # euc-kr, utf-8: 둘다 한글 인코딩방식 , 차이점은 둘의 글자당 바이트 수가 다름(utf-8은 3바이트이며 국제표준 한글표기, euc-kr은 국내표준 한글표기)
# with open('1.txt','r',encoding='utf8') as file:
#     print(file.read())
    
# 파일 한번에 읽어오기
with open('1.txt','r',encoding='utf8') as file:
    lines=file.readlines()
    for line in lines:
        print(line,end='')

# 파일 삭제
os.remove('1.txt')


# with open('1.txt','r',encoding='utf8') as file:
#     print(file.readline(),end='') # readline은 자동으로 줄바꿔줌, 게다가 write할때 \n으로 줄바꿈을 해줬기때문에 두줄 생김
#     print(file.readline(),end='')
#     print(file.readline(),end='')
#     print(file.readline(),end='')
#     print(file.readline(),end='')
#     print(file.readline(),end='')

# # 파일의 내용을 1줄씩 읽어오기    
# with open('1.txt','r',encoding='utf8') as file:
#     while True:
#         line=file.readline()
#         if not line:
#            break
#         print(line,end='')
         
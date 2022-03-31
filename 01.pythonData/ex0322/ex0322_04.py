import os # 윈도우 탐색기 같은 기능 (폴더를 수정할 때 사용)

with open('1.txt','w',encoding='utf8') as file: # 컴퓨터가 종료되어도 파일은 지워지지 않는다
  file.write('1\t홍길동\t100\t100\t200\t100.0\t0\n')  
  file.write('2\t이순신\t100\t100\t200\t100.0\t0\n')  
  file.write('3\t유관순\t100\t100\t200\t100.0\t0\n')  
  file.write('4\t강감찬\t100\t100\t200\t100.0\t0\n')  
  file.write('5\t김구\t100\t100\t200\t100.0\t0\n')  




# file = open('1.txt','w',encoding='utf8')
# file.write('글을 다른형태로 쓰기합니다.\n')
# file.close() # with말고 open을 파일로 직접 지정하면 반드시 마지막에 close()로 닫아줘야함


# with open('1.txt','w',encoding='utf-8') as file: # w: write (덮어쓰기), a: 현재글에 추가, r: read #open에 있는 정보를 file에 넣어라
#     file.write('파이썬수업이 진행중입니다.\n')
#     file.write('현재 모듈수업입니다.\n')
#     file.write('file저장입니다.\n')

# with open('1.txt', 'a',encoding='utf-8') as file:
#     file.write('다시 글을 입력합니다.\n')

# print(os.name)
# print(os.getcwd()) # 현재위치
# print(os.listdir()) # 현대 폴더안에 무슨 폴더가 있는지 출력

# os.mkdir('hello') # 폴더 생성함수
# os.rmdir('hello') # hello라는 폴더 삭제, 폴더 삭제함수
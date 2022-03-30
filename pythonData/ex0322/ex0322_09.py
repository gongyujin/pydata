from tempfile import strInput,strFileSave
# print(os.listdir())
# 파일이 있으면 파일이름을 1_1.txt로 변경해서 저장하시오.
# 1. 파일이름을 1.txt
# 2. 내용은 "파일이름저장완료" 글자를 저장
# 3. 파일을 저장
# 조건: 동일한 파일이름이 있으면
# 파일이름을 1_1.txt 변경해서 저장시키시오.
# # 동일한 파일이름이 없으면 1.txt 저장시키시오.
# 옵션1
# 저장할 내용도 입력을 받고
# 저장할 파일이름도 입력을 받아 저장시키시오.

str1=''
content=[]

# 파일이름, 파일내용을 입력받는 함수
str1=strInput(str1,content) # 변수는 무조건 반환해야함

# 파일저장 함수
strFileSave(str1,content)

#-------------------------------------------------------------------------  
# if '1.txt' in os.listdir():
#     print('있습니다.')
#     with open('1.txt','a',encoding='utf8') as file:
#         file.write('파일을 추가해서 저장시킵니다.\n')
# else:
#     print('없습니다.')
#     with open('1.txt','w',encoding='utf8') as file:
#         file.write('파일을 새로만들어서 저장시킵니다.\n')
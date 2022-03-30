# 입력된 문자의 시작이 >>로 시작하는지 확인해서 
# >>로 시작하지 않으면 >>를 입력하세요.

str1=input('문자를 입력하세요.>> ')
if str1.startswith('>>'):
    print(str1)
else:
    print('>>'+str1,end='')


# # 입력된 문자의 첫글자가 대문자인지 확인해서 대소문자를 판별하라
# # 대문자입니다. 출력하시오.



# while True:
#     str1=input('문자를 입력하세요.>> ')
#     if str1[0].isupper():
#         print('첫글자는 대문자입니다. 출력하시오')
        
#     else:
#         print('첫글자는 대문자가 아닙니다.')
#     print()
    

# str1='aaa'
# print(str1.startswidth(''))  # 특정한 문자랑 비교해야하기 때문에 빈칸으로 할 순 없음
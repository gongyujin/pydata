str1='PYTHON Is easy'

# 대소문자 구분함
print(str1.startswith('P')) # 첫부분 확인
print(str1.endswith('Y')) # 끝부분 확인

# # 대소문자 구분없이 python 검색

# inStr=input('문자를 입력하세요.>> ')
# if inStr.lower() in str1.lower():
#     print('{}는 존재합니다.'.format(inStr))
# else:
#     print('{}은 글자가 없습니다.'.format(inStr))



# print(str1.count('s')) # 똑같은 s글자가 몇개 있는가

# print(str1.find('t')) # 몇번재 자리에 있는가
# print(str1.find('b'))
# print(str1.index('t'))
# if  'th' in str1:
#     print(str1.index('th'))
# else:
#     print('없습니다.')



# print(str1.upper()) # 대문자
# print(str1.lower()) # 소문자
# print(str1.swapcase()) # 소문자 -> 대문자, 대문자 -> 소문자
# print(str1.title()) # 단어의 첫글자를 대문자로
# print(str1.isupper) # 첫글자가 대문자인지 확인: True or False
# # 정규표현식


# list1=[10,4,3,9,20,21]
# list2=[21,20,9,3,4,10] # 역순출력
# list3=[3,4,9,10,20,21] # 순차정렬
# list4=[21,20,10,9,4,3] # 역순정렬

# list1.reverse()
# print(list1)
# list1.sort(reverse=True)
# print(list1)


# inStr, outStr = '',''
# count,i = 0,0

# inStr = input('원하는 글자를 입력하세요.>> ')
# count=len(inStr)

# for i in range(0,count):
#     outStr += inStr[(count-1)-i)] #append라고 하지 않아도 더해도 문자열을 만들수 있다

# print(outStr)


#str1='서울인재개발원 파이썬수업'
# for i in range(len(str1)):
#     if i == 0:
#         print(str1[i],end='')
#     else:
#         print(','+str1[i],end='')


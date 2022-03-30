# 주민번호 뒤자리를 입력받아 남자,여자를 출력하시오.
# 7자리가 아니면 다시 입력받아라
# 990101-1105555
# 1,3이면 남자 2,4이면 여자--> 아니라면 다시입력받음

# while True:
#     number=input('주민번호를 입력하세요.>> ')
#     if len(number)==14:
        
#         if number[7]=='1' or number[7]=='3':
#             print('남자입니다.')
#             break
#         elif number[7]=='2' or number[7]=='4':
#             print('여자입니다.')
#             break
#         else:
#             print('뒤자리가 틀렸습니다. 다시입력하세요.')
#     else:
#         print('주민번호가 틀렸습니다. 다시입력하세요.')
#         continue   


while True:
    number=input('주민번호 뒤 7자리를 입력하세요.>> ')
    if len(number)!=7:
        print('7자리가 아닙니다. 다시입력하세요.')
        continue
        
    if number[0]=='1' or number[0]=='3':
        print('남자입니다.')
        break
    elif number[0]=='2' or number[0]=='4':
        print('여자입니다.')
        break
    else:
        print('뒤자리가 틀렸습니다. 다시입력하세요.')
            
        



# # 문자열 슬라이싱
# str1 = '안녕하세요. 파이썬입니다.'
# print(str1[7:]) # 리스트랑 같이 슬라이싱할 수 있음
# print(str1[2])

# str-len()함수
# alist=[123,46,3451,483,1,50,111,33333,9,1000000]
# numlist=['짝수','홀수']

# # 123[3자리]: 홀수
# # 45[2자리]: 홀수

# for i in alist: # if문을 많이 쓰면 속도가 느려짐
#     # if i % 2 ==0:
#     print('{:7d}[{}자리] : {}'.format(i,len(str(i)),numlist[i%2]))
#     # else:
#     #     print('{:7d}[{}자리] : {}'.format(i,len(str(i)),'홀수'))



# a='안녕하세요. 파이썬수업에 오신것을 환영합니다.' # 문자열은 list 타입과 같다
# alist=[1,2,3,4,5]
# print(alist[2])
# print(a[2])

# print(len(alist))
# print(len(a))
dd='a1aaaabb' # 대소문자를 구분하는 것이기 때문에 숫자가 들어가도 괜찮음, lower(): 소문자인지 비교, isupper(): 대문자인지 비교
if dd.islower():
    print('소문자입니다.')
else:
    print('소문자가 아닙니다.')


# cc='a1b2c3!' # 특수문자는 해당하지 않기 때문에 특수문자가 있는지 없는지 확인할 수 있음
# if cc.isalnum(): # 문자, 또는 숫자인지 비교
#     print('문자 또는 숫자입니다.')
# else:
#     print('문자 똔느 숫자가 아닙니다.')


# bb='abc'
# if bb.isalpha(): #문자인지 비교
#     print('문자입니다.')
# else:
#     print('문자가 아닙니다.')
    
# aa='1234ㅁ'
# if aa.isdigit(): #숫자인지 비교
#     print('숫자입니다.')
# else:
#     print('숫자가 아닙니다.')
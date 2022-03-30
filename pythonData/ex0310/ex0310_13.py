id='aaa'
pw='1111'

user_id = input('아이디를 입력하세요.>> ')
user_pw = input('패스워드를 입력하세요.>> ')

# if id==user_id:
#     print('아이디가 같습니다.')
#     if pw==user_pw:
#         print('패스워드가 같습니다.')
#         print('로그인 되었습니다.')
#     else:
#         print('패스워드가 일치하지 않습니다.\n다시 입력하세요.!')
# else:
#     print('아이디가 일치하지 않습니다. \n다시 입력하세요.!')

# if (id==user_id and pw==user_pw):
#     print('아이디, 패스워드가 일치합니다. 로그인되었습니다.')
# else:
#     print('아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요.!!')

if (id==user_id or pw==user_pw):
    print('아이디 또는 패스워드가 일치합니다.')
else:
    print('아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요.!!')
    
# 숫자가 들어가면 ture라고 보지만 0이 들어가면 false라고 봄

    
    
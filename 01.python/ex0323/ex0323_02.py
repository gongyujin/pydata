while True:
    try:
        a=int(input('숫자를 입력하세요.>>'))
        print(a)
    except Exception as err: # error 메세지를 출력하기 위해서 exception을 사용함
        print(err)
        print('예외가 발생되었습니다.')

# a = int(input('정수를 입력하세요.>>'))
# print(a)
# # try:
# #     a = int(input('정수를 입력하세요.>>'))
# #     print(a)
# # except:
# #     print('print명령은 완벽합니다.')
    
# print('프로그램을 종료합니다.')    
# except라고만 하면 모든 예외처리
# valueerror: 문자인지 판별가능
try:
    input1=int(input('1숫자를 입력하세요.>>'))
    input2=int(input('2숫자를 입력하세요.>>'))
    print(input1/input2)
# except ValueError:
#     print('숫자가 아닙니다.')
# except ZeroDivisionError:
#     print('0으로 나누기는 불가능합니다.')
except Exception as err:
    print(err)
    print('모든 에러를 다 처리할 수 있습니다.')    

print('프로그램 종료')
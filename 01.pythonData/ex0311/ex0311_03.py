score=int(input('점수를 입력하세요.>> '))

msg='' # 초기값을 설정해줘야 error가 나오지 않음 , 전역변수
if score >= 60:
    msg='합격' #if 범위에 성립되지 않아서 들어가지 않으면 변수 선언이 되지않기 때문에 defined, if안에 있기때문에 지역변수라고 함
else:
    msg='불합격'

msg='합격' if score>=60 else '불합격' #한줄로 표현할 수 있음 , 변수가 한개고 짧을때만 사용
print(msg)
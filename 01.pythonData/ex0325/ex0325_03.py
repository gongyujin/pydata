from stumanage.student import Student

s2=Student('홍길동', 100, 100)
s1=Student()
s1.stuname='홍길동'

# 주소값을 비교하는 것 단, __eq__로 정의해서 이름으로 비교할 수 있음
if s1==s2: # s1=='홍길동' 하면 객체와 스트링비교여서 에러남 (대신 클래스에서 other.stuname을 other로 바꾸면 에러안남)
    print('동일한 사람입니다. 이름 :', s1.stuname)
else:
    print('이름이 없습니다.')
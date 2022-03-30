# frome datetime import *
import datetime
now =datetime.datetime.now()
year=now.year
month=now.month +1
day=now.day
hour=now.hour
minute=now.minute
second=now.second
print('{}-{}-{} {}:{}:{}'.format(year,month,day,hour,minute,second))
print(now)

# # print(dir(datetime)) # 모듈에 있는 라이브러리함수를 확인
# stuSave=[]
# stuname=input('이름을 입력하세요.>> ')
# now=datetime.datetime.now()
# temp={'stuname':stuname,'inputTime':'{}-{:02d}-{}'.format(now.year,now.month,now.day)}

# stuSave.append(temp)
# print(stuSave)

# ip: 인터넷 개인주소
# dns: 한글, 영문주소 ex)naver.com
# port: 컴퓨터내 프로그램주소 ex) 한글 1001 웹 80 오라클 8080
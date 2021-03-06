#  파일첨부 이메일 발송

import smtplib
# MIME 객체 - 보내는 사람, 받는사람, 내용
from email.mime.text import MIMEText 
# MIME 객체 - 보내는 사람, 받는사람, 내용, 파일첨부
from email.mime.multipart import MIMEMultipart 
# 파일첨부하는 라이브러리
from email.mime.base import MIMEBase
# 파일첨부한 내용을 인코딩
from email import encoders

smtpName='smtp.gmail.com'
smtpPort=587
sendEmail='gongyujin98@gmail.com'
password="16자리 입력"
recvEmail='gyuj0114@naver.com'

title='주식시세 1-200위까지 파일첨부함.'
content='시가총액 1위에서 200위까지 주식시세를 파일 첨부해서 보냅니다.'

# msg=MIMEText(content) #multipart로 바뀜
# MIME 객체생성
msg=MIMEMultipart('alternative')
part2=MIMEText(content)

msg.attach(part2)
msg['From']=sendEmail
msg['To']=recvEmail
msg['Subject']=title

# 파일첨부
part=MIMEBase('application','octet-stream')
# 파일읽어오기
with open('시가총액1-200.csv','rb') as f:
    # part에 파일담기
    part.set_payload(f.read())
    
# 파일첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)

# header정보 정의
part.add_header('Content-Disposition','attachment',filename='시가총액1-200.csv')


# content, 첨부파일을 attach추가
msg.attach(part)

# 메일서버 정보
s=smtplib.SMTP(smtpName,smtpPort)
# s.ehlo() # 서버 연결을 설정하는 단계
s.starttls() # 서버접근
s.login(sendEmail,password) # 서버로그인
# 메일 발송(보내는 주소, 받는 주소, 내용)
s.sendmail(sendEmail,recvEmail,msg.as_string())

print('메일발송이 완료되었습니다.')
s.close()








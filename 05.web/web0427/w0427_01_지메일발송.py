from calendar import c
from operator import concat
import smtplib
from email.mime.text import MIMEText

# gmail 이메일 서버 사용방법
# naver와 동일
# google 계정관리 --> 보안 클릭
# password 2단계 인증 --> 앱 비밀번호 16자리 사용
# 토큰 키 생성후 사용하면 발송됨
# smtp.gmail.com:587



# smtp 서버명
smtpName="smtp.gmail.com"
smtpPort=587

sendEmail="gongyujin98@gmail.com"
password="1111"
recvEmail="gyuj0114@naver.com"


# 글자
title="gmail발송제목"
content="gmail 발송내용입니다."

# MIME 객체
msg=MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['subject']=title

# 메일서버 정보
s=smtplib.SMTP(smtpName,smtpPort)
# s.ehlo() # 서버 연결을 설정하는 단계
s.starttls() # 서버접근
s.login(sendEmail,password) # 서버로그인
# 메일 발송(보내는 주소, 받는 주소, 내용)
s.sendmail(sendEmail,recvEmail,msg.as_string())

s.close()
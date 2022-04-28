# 메일발송 라이브러리
import smtplib
from email.mime.text import MIMEText # 글자를 보낼때 사용

smtpName="smtp.naver.com" # 메일서버주소
smtpPort=587 # 메일서버 포트번호


sendEmail="gyuj0114@naver.com" # 자신의 아이디
password="1111" # 자신의 비밀번호
recvEmail="mayitshe87@naver.com" # 받는사람 주소


# 글쓰기 제목, 내용
title="파이썬 이메일 보내기 수업"
content='파이썬 수업이 진행중입니다. 현재 38일차입니다.'

# MIME 객체
msg=MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['Subject']=title


# 메일서버주소 정보 예시) smtp.naver.com/587
s=smtplib.SMTP(smtpName,smtpPort)
# 메일서버접근
s.starttls()
# 메일서버로그인
s.login(sendEmail,password)
# 메일발송
s.sendmail(sendEmail,recvEmail,msg.as_string())
# 메일 닫기
s.close()
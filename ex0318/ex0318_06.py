# 입력은 url을 입력받음
# url=input('url을 입력하세요.>> ')
url='http://www.naver.com'
# 힌트: http://wwww. 는 replace, .com은 index, find 사용
# naver+글자총길이수+c가 들어간 개수+!!
# 예) 비밀번호 생성: pw=naver201!!
dis=len(url)
reurl=url.replace('http://www.','')
name=reurl[:reurl.index('.')]

count=url.count('c')

print('비밀번호생성: {}{}{}{}'.format(name,dis,count,'!!'),end='')

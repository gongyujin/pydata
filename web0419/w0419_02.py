from urllib import request
import requests

# res=requests.get("http://www.naver.com")
res=requests.get("https://www.melon.com")
res.raise_for_status() # 코드200이 아니면 프로그램을 자동종료
# res.status_code : 200,403,404,....
# 200: 정상코드
# 403, 406: 접근권한이 없음, 권한을 막았을 때 403에러뜸
# 404: 페이지 없음 에러
# 500이상: 프로그램에서 에러
if res.status_code == requests.codes.ok:
    # if res.statue_code == 200:와 같은 의미
    print('정상적으로 페이지가 열립니다.')
else:
    print('페이지에 문제가 있습니다.')
    
    
print(res.text)
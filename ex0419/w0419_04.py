import requests
import re # 정규표현식 라이브러리

url="http://www.google.com"
res=requests.get(url) # url 파일 정보가져오기
res.raise_for_status() # 200코드 확인

p=re.compile('ca.e')
# temp=input('글자를 입력하세요.>> ')

# m=p.match("good care good cafe") 
# # match, search, findall: complie로 만들었을때만 사용할 수 있음 
# # match: 처음부터 정확히 일치해야지만 찾아짐. search : 단어 내에 포함되어 있으면 찾아짐.
# match는 첫번째 단어에서만 확인함 ==> good care를 체크하게되면 good만 확인하기 때문에 찾을 수 없음
# search는 모든 단어를 체크함. 단, 앞단어가 일치한다면 뒤 단어도 일치해도 체크하지 못함
# findall는 전체를 체크함, 리스트 형태

# group: 일치하는 문자열 반환, string: 입력받은 문자열 반환, 
# start: 일치하는 시작 index (위치알려줌), end: 일치하는 끝 index, span: 시작과 끝의 index
# if m:
#     print('매칭 단어 : ', m.group()) 
# else:
#     print('매칭되는 단어가 아닙니다.')

m=p.findall('morning good care')
print(m)

if len(m)==0:
    print("매칭되는 단어가 없습니다.")
else:
    print('매칭되는 단어가 있습니다.')
    
    
# image=""
# p=re.compile('^/images') #^~: ~으로 시작하는지
# m=p.match("/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png")
# if m:
#     print('http://www.google.com'+m.group())
# else:
#     print('매칭되는 태그가 없습니다.')

# # 정규표현식
# p=re.compile('ca.e') # 정규표현식 세팅/ caffe는 두글자이기 때문에 불가능
# temp=input('정규표현식과 일치하는지 확인합니다. 문자를 입력하세요.>> ')
# m=p.match(temp) # 입력된 문자 case가 정규표현식과 일치하는지 확인 (정확하게 일치하는지 확인)
# if m:
#     print("일치하는 문자 : ",m.group()) # 들어있는 문자를 모두 출력
# else:
#     print('해당문자는 일치하지 않습니다.')


# if res.status_code == requests.codes.ok:
#     print('정상입니다.')
# else:
#     print('비정상입니다.')
    
    
# print(res.text)
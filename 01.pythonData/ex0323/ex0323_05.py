from urllib import request
# url을 가져와서 가공해주게 하는것

rs=request.urlopen('https://www.naver.com/')
print(rs.read())

# import time

# print('프로그램시작')
# print('cat은 무슨뜻일까요?')
# time.sleep(5) #시간딜레이 해줌
# print('고양이 입니다.')
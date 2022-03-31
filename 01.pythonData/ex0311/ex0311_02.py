import datetime 
#날짜를 뽑아내는 것

now= datetime.datetime.now()
# 12,1,2 : 겨울입니다.
# 3,4,5: 봄입니다.
# 6,7,8: 여름입니다.
# 9,10,11: 가을입니다.

num_month=now.month
if num_month==12 or 1<= num_month <=2:
    print('겨울입니다.')
elif num_month <=5:
    print('봄입니다.')
elif num_month <=8:
    print('여름입니다.')
else:
    print('가을입니다.')


now1=int(input('입력할 월을 입력하세요.>> '))
if now1==12 or 1<= now1 <=2:
    print('겨울입니다.')
elif now1 <=5:
    print('봄입니다.')
elif now1 <=8:
    print('여름입니다.')
elif now1 <=11:
    print('가을입니다.')
else:
    print('정확한 월의 입력이 아닙니다. 오류입니다.')
    
    
    
# print(now)
# #현재 연도, 월, 일, 시, 분, 초
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

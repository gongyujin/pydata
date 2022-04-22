import re

rate="후기평점 4.8점"

# sub(): string에서 pattern과 일치하는 문자들을 지정하는 형태로 교체
# re.sub(r'[패턴-정규표현식]','해당부분을 교체할 내용',rate) / 정규표현식이 맞으면 교체할 내용이 나옴
re_rate=re.sub(r'[^0-9.]','',rate) # sub안에서 ^는 not을 의미하고, complie안에서 ^은 시작을 의미함
print(re_rate)

text='123abc456'
re_text=re.sub(r'[^0-9]','',text) #[0-9a-zA-Z] ==> 문자의 집합을 의미
print(re_text)
# rate=rate[5:8]
# print("평점 : ",rate)

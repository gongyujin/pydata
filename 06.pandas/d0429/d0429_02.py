import pandas as pd
import re

df=pd.read_excel('stat_142801.xls',skiprows=2,index_col=0,nrows=2)

# print(df.loc['출생아\xa0수'])
df.index.name='목록'

for i in range(len(df.index)):
    # \d: 숫자를 [0-9]와 동일
    # \D: 숫자가 아닌 문자 [^0-9]와 동일
    # \s: 공백 문자(띄어쓰기, 탭, 엔터 등)
    # \S: 공백이 아닌 문자
    # \w: 알파벳대소문자, 숫자 [0-9a-zA-Z]와 동일
    # \W: non alpha-numeric 문자 [^0-9a-zA-Z]와 동일
    
    df.rename(index={df.index[i]:re.sub(r'[\s]','',df.index[i])},inplace=True) # \s:빈공백만 제거, \S:빈공백이 아닌것만 제거
    # df.rename(index={df.index[i]:re.sub(r'[^ㄱ-힣]','',df.index[i])},inplace=True) # 한글만 남기고 모두 제거
print(df.index.values)
print(df.loc['출생아수'])

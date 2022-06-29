import requests
from bs4 import BeautifulSoup

response=requests.get('http://www.nalthin.com/cal/e.html')
print(response.content)
soup=BeautifulSoup(response.content,'html.parser')
print(type(soup))

# import requests

# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

# res=requests.get("https://www.melon.com",headers=headers)
# res.raise_for_status()
# with open('cal_test.html','w',encoding='utf-8') as f:
#     f.write(res.text)


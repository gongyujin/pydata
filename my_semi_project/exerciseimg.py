import requests
import json
from pprint import pprint
import csv

filename='exercise_img.csv'

f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)
title='id,uuid,exercise_base,image'.split(',')
writer.writerow(title)

# url = "https://fitness-calculator.p.rapidapi.com/bodyfat"
url= "https://wger.de/api/v2/exerciseimage/"
querystring = {"key":"value"}

headers = {
	"Accept": "application/json",
	"Authorization": "a83b51b5374548c88820974a05f9746d63399a10"
}
response = requests.request("get",url,  params=querystring, headers=headers)
# print(literal_eval(response.text))

total_res=json.loads(response.content)

res=total_res['results']
print(res)

for row in res:
    id=row['id']
    uuid=row['uuid']
    base=row['exercise_base']
    href=row['image']
    
    data=[]
    data.append(id)
    data.append(uuid)
    data.append(base)
    data.append(href)
    writer.writerow(data)

    
while total_res['next']:
    next=total_res['next'] # 다음페이지 이동
    url= next
    querystring = {"key":"value"}
    headers={"Accept": "application/json","Authorization": "a83b51b5374548c88820974a05f9746d63399a10"}
    response = requests.request("get",url,params=querystring, headers=headers)
    total_res=json.loads(response.content)
    res=total_res['results']
    
    print(res)
    for row in res:
        id=row['id']
        uuid=row['uuid']
        base=row['exercise_base']
        href=row['image']
        
        data=[]
        data.append(id)
        data.append(uuid)
        data.append(base)
        data.append(href)
        writer.writerow(data)
    
f.close()    
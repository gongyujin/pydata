import requests
from ast import literal_eval
import json
from pprint import pprint
import csv

filename='exercise.csv'

f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)
title='id,uuid,name,exercise_base,description,category,muscles,muscles_secondary,equipment'.split(',')
writer.writerow(title)


# url = "https://fitness-calculator.p.rapidapi.com/bodyfat"
url= "https://wger.de/api/v2/exercise/"
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
    name=row['name']
    base=row['exercise_base']
    description=row['description']
    category=row['category']
    muscles=row['muscles']
    secondary=row['muscles_secondary']
    equipment=row['equipment']
    
    data=[]
    data.append(id)
    data.append(uuid)
    data.append(name)
    data.append(base)
    data.append(description)
    data.append(category)
    data.append(muscles)
    data.append(secondary)
    data.append(equipment)
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
        name=row['name']
        base=row['exercise_base']
        description=row['description']
        category=row['category']
        muscles=row['muscles']
        secondary=row['muscles_secondary']
        equipment=row['equipment']
        
        data=[]
        data.append(id)
        data.append(uuid)
        data.append(name)
        data.append(base)
        data.append(description)
        data.append(category)
        data.append(muscles)
        data.append(secondary)
        data.append(equipment)
        writer.writerow(data)
    

f.close()
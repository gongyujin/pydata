import requests
import json
from pprint import pprint
import csv
filename='exercise_base.csv'

f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)
title='id,uuid,category,muscles,equipment,images,ex_id,ex_name,description'.split(',')
writer.writerow(title)

# url = "https://fitness-calculator.p.rapidapi.com/bodyfat"
url= "https://wger.de/api/v2/exercisebaseinfo/"
querystring = {"key":"value"}

headers = {
	"Accept": "application/json",
	"Authorization": "a83b51b5374548c88820974a05f9746d63399a10"
}

response = requests.request("get",url,  params=querystring, headers=headers)

total_res=json.loads(response.content)
res=total_res['results']
print(res)

for row in res:
    id=row['id']
    uuid=row['uuid']
    category=row['category']['name']
    
    if row['muscles']:
        muscles=row['muscles'][0]['name_en']
    else:
        muscles=[]
    if row['images']:
        images=row['images'][0]['id']
    else:
        images=[] 
    
    if row['equipment']:
        equipment=row['equipment'][0]['name']
    else:
        equipment=[]
    ex_id=row['exercises'][0]['id']
    ex_name=row['exercises'][0]['name']
    description=row['exercises'][0]['description']

    
    data=[]
    data.append(id)
    data.append(uuid)
    data.append(category)
    data.append(muscles)
    data.append(equipment)
    data.append(images)
    data.append(ex_id)
    data.append(ex_name)
    data.append(description)
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
        category=row['category']['name']
        
        if row['muscles']:
            muscles=row['muscles'][0]['name_en']
        else:
            muscles=[]
        if row['images']:
            images=row['images'][0]['id']
        else:
            images=[] 
        
        if row['equipment']:
            equipment=row['equipment'][0]['name']
        else:
            equipment=[]
        ex_id=row['exercises'][0]['id']
        ex_name=row['exercises'][0]['name']
        description=row['exercises'][0]['description']

        
        data=[]
        data.append(id)
        data.append(uuid)
        data.append(category)
        data.append(muscles)
        data.append(equipment)
        data.append(images)
        data.append(ex_id)
        data.append(ex_name)
        data.append(description)
        writer.writerow(data)
      

f.close()
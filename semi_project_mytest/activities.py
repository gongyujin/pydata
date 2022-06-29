# For activity level :
# "1" : "BMR",
# "2" : "Sedentary: little or no exercise",
# "3" : "Exercise 1-3 times/week",
# "4" : "Exercise 4-5 times/week",
# "5" : "Daily exercise or intense exercise 3-4 times/week",
# "6" : "Intense exercise 6-7 times/week",
# "7" : "Very intense exercise daily, or physical job"
# For goals :
# "maintain" : "maintain weight",
# "mildlose" : "Mild weight loss",
# "weightlose" : "Weight loss",
# "extremelose" : "Extreme weight loss",
# "mildgain" : "Mild weight gain",
# "weightgain" : "Weight gain",
# "extremegain" : "Extreme weight gain"

import requests
from ast import literal_eval
import csv

filename='activity.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)
title='_id,id,activity,metValue,intensityLevel,name'.split(',')
writer.writerow(title)


url = "https://fitness-calculator.p.rapidapi.com/activities"

lists=["2","3","6"]
for list in lists:
	querystring = {"intensitylevel":list}

	headers = {
		"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
		"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	dic1=literal_eval(response.text)['data']
	print(len(dic1))
	print(dic1[0]['_id'])
	print(dic1[0]['id'])
	print(dic1[0]['activity'])
	print(dic1[0]['metValue'])
	print(dic1[0]['description'])
	print(dic1[0]['intensityLevel'])
	print(dic1)

	for row in dic1:
		id1=row['_id']
		id2=row['id']
		act=row['activity']	
		met=row['metValue']
		level=row['intensityLevel']
		description=row['description']
	
		names=description.split(',')[0]
		# for name in names:
		# 	data=[]
		# 	data.append(id1)
		# 	data.append(id2)
		# 	data.append(act)
		# 	data.append(met)
		# 	data.append(level)
		# 	data.append(name)
		# 	writer.writerow(data)
		data=[]
		data.append(id1)
		data.append(id2)
		data.append(act)
		data.append(met)
		data.append(level)
		data.append(names)
		writer.writerow(data)
		
f.close()
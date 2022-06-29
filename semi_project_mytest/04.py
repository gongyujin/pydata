# daily calory requirements
# 내 activity level을 기반으로 7개의 goal에 따른 하루 calory 섭취량과 몸무게변화량

import requests

url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"

querystring = {"age":"25","gender":"male","height":"173","weight":"57","activitylevel":"level_3"}

headers = {
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
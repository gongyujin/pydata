# body fat percentage 체지방률

import requests
from ast import literal_eval

url = "https://fitness-calculator.p.rapidapi.com/bodyfat"

querystring = {"age":"25","gender":"female","weight":"57","height":"173","neck":"50","waist":"96","hip":"92"}

headers = {
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
}

response = requests.request("GET", url, headers=headers, params=querystring)

dic1=literal_eval(response.text)['data']
print(dic1['Body Fat (U.S. Navy Method)']) # 체지방률
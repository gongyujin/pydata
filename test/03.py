# macros amounts
# 입력값 : 나이, 성별, 키, 몸무게, 운동강도, 목표

import requests

url = "https://fitness-calculator.p.rapidapi.com/macrocalculator"

querystring = {"age":"25","gender":"female","height":"173","weight":"57","activitylevel":"5","goal":"extremelose"}

headers = {
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
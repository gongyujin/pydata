# ideal weight
# 입력한 성별과 키에 맞춰서 4가지 수식을 이용하여 이상적인 몸무게를 제시

import requests

url = "https://fitness-calculator.p.rapidapi.com/idealweight"

querystring = {"gender":"female","height":"173"}

headers = {
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
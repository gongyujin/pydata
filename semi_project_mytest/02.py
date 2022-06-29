# bmi
# 내 bmi 지수/ 나의건강상태(저체중,정상,과체중)/내가 해당하는 상태에서 bmi 지수
import requests

url = "https://fitness-calculator.p.rapidapi.com/bmi"

querystring = {"age":"25","weight":"57","height":"173"}

headers = {
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
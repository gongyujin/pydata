# burned calorie from activity
# 칼로리를 얼마나 태울수 있는지 보여줌
import requests

url = "https://fitness-calculator.p.rapidapi.com/burnedcalorie"

querystring = {"activityid":"bi_1","activitymin":"60","weight":"75"}

headers = {
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
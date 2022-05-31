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

url = "https://fitness-calculator.p.rapidapi.com/activities"

querystring = {"intensitylevel":"6"}

headers = {
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "091f953142mshbaea248d7caa5bdp10e907jsn608af64e4544"
}

response = requests.request("GET", url, headers=headers, params=querystring)
dic1=literal_eval(response.text)
print(len(dic1['data']))
print(dic1['data'])
# print(soup)
import requests
import json
from pprint import pprint

# url = "https://fitness-calculator.p.rapidapi.com/bodyfat"
url= "https://wger.de/api/v2/equipment/"
querystring = {"key":"value"}

headers = {
	"Accept": "application/json",
	"Authorization": "a83b51b5374548c88820974a05f9746d63399a10"
}

response = requests.request("get",url,  params=querystring, headers=headers)
print(response.text)
# print(literal_eval(response.text))
pprint(json.loads(response.content)['results'])
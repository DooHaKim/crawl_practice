import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("https://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    print(responseJson)
    return responseJson.get("country_code")

print(getCountry("222.104.162.107"))
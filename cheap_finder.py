import urllib.request
import json

def dataGet():

    url = 'https://api.crypto-bridge.org/api/v1/ticker'
    readObj = urllib.request.urlopen(url)
    response = readObj.read()

    return response


def jsonConversion(jsonStr):

    data = json.loads(jsonStr)

    return data


resStr = dataGet()
res = jsonConversion(resStr)

for ticker in res: 
    print(ticker['id'] + ':' + ticker['bid'])
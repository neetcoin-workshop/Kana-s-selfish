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


#BTC価格の抽出とソート
def sortByPrice(list_org):
    list_BTC = []

    for list_all in list_org:
        if '_BTC' in list_all['id']:
            list_BTC.append(list_all)

    list_BTC_sorted = sorted(list_BTC, key = lambda x:x['bid'])

    return list_BTC_sorted


resStr = dataGet()
res = jsonConversion(resStr)
ticker_BTC = sortByPrice(res)

for price in ticker_BTC:
    print(price['id'] + ':' + price['bid'])



import urllib.request as urllib2
import json

def convert_to_bitcoin(amount, currency):
    api="https://blockchain.info/tobtc?currency="+str(currency)+ "&value="+str(amount)
    data = urllib2.urlopen(api)
    converted = json.loads(data.read())
    print(int(converted*100000000))


convert_to_bitcoin(1, "USD")
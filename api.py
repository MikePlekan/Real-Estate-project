import http.client
import json
import pprint
conn = http.client.HTTPSConnection("api.gateway.attomdata.com")

headers = { 
    'accept': "application/json", 
    'apikey': "", 
} 

conn.request("GET", "/propertyapi/v1.0.0/sale/snapshot?latitude=30.2500&longitude=-97.7500&radius=200&orderBy=saleAmt+desc&pageSize=50", headers=headers)

res = conn.getresponse()
data = res.read()
data=json.loads(data.decode("utf-8"))

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)

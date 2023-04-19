import http.client
import json
import pprint
conn = http.client.HTTPSConnection("api.gateway.attomdata.com")

headers = { 
    'accept': "application/json", 
    'apikey': "", 
} 

conn.request("GET", "/v4/neighborhood/community", headers=headers)

res = conn.getresponse()
data = res.read()
data=json.loads(data.decode("utf-8"))

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)

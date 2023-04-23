import http.client
import json
import pprint
# conn = http.client.HTTPSConnection("api.gateway.attomdata.com")

# headers = { 
#     'accept': "application/json", 
#     'apikey': "2b1e86b638620bf2404521e6e9e1b19e", 
# } 

# conn.request("GET", "/propertyapi/v1.0.0/sale/snapshot?latitude=30.2500&longitude=-97.7500&radius=200&orderBy=saleAmt+desc&pageSize=50", headers=headers)

# res = conn.getresponse()
# data = res.read()
# with open("data.json", "w") as outfile:
#     outfile.write(data.decode("utf-8"))
# data=json.loads(data.decode("utf-8"))

# Opening JSON file
with open('data.json', 'r') as openfile:
 
    # Reading from json file
    data = json.load(openfile)
[x.pop("location") for x in data['property']]
[x.pop("lot") for x in data['property']]
[x.pop("vintage") for x in data['property']]
pp = pprint.PrettyPrinter(indent=2)
with open("dict1.txt", "w") as outfile:
    outfile.write(pp.pformat(data))


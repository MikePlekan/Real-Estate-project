import http.client
import json
import pandas as pd
import random
zips=pd.read_csv('zip.csv')
df=pd.DataFrame(columns=['countrySubd', 'locality', 'attomId','saleTransDate','proptype','yearbuilt'])
sales=pd.DataFrame(columns=['saleamt','attomId'])
for x in random.sample(zips['zipcode'].to_list(),10):

    conn = http.client.HTTPSConnection("api.gateway.attomdata.com")
    headers = { 
        'accept': "application/json", 
        'apikey': "2b1e86b638620bf2404521e6e9e1b19e", 
    }
    conn.request("GET", "/propertyapi/v1.0.0/sale/snapshot?postalcode=12309&postalcode=12211&minUniversalSize=0&maxUniversalSize=7000&pageSize=500", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data=json.loads(data.decode("utf-8"))
# with open("data2.json", "w") as outfile:
#     outfile.write(data.decode("utf-8"))
# data=json.loads(data.decode("utf-8"))

# # Opening JSON file
# with open('data2.json', 'r') as openfile:
 
#     # Reading from json file
#     data = json.load(openfile)
    [x.pop("location") for x in data['property']]
    [x.pop("lot") for x in data['property']]
    [x.pop("vintage") for x in data['property']]

    for x in data['property']:
        if(x['building'].get('rooms')!=None and x['building'].get('rooms').get('beds')!=None and x['building'].get('rooms').get('bathstotal')!=None and x['sale']['amount'].get('saleamt')!=None):
            temp=pd.DataFrame({'countrySubd':[x['address'].get('countrySubd')],
                            'locality':[x['address'].get('locality')],
                            'attomId':[x['identifier'].get('attomId')],
                            'saleTransDate':[x['sale'].get('saleTransDate')],
                            'proptype':[x['summary'].get('proptype')],
                            'yearbuilt':[x['summary'].get('yearbuilt')],
                            'universalsize':[x['building'].get('size').get('universalsize')],
                            'beds':[x['building'].get('rooms').get('beds')],
                            'bathstotal':[x['building'].get('rooms').get('bathstotal')]})
            df=pd.concat([df,temp],ignore_index=True)
            temps=pd.DataFrame({'saleamt':[x['sale']['amount'].get('saleamt')],'attomId':[x['identifier'].get('attomId')]})
            sales=pd.concat([sales,temps],ignore_index=True)
df.to_csv('data.csv')
sales.to_csv('sales.csv')



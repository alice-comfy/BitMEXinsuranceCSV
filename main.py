import requests
import json
import pandas as pd
#fetch fund balance from API, can only do 500 at once
def get_Ins(start):
    cur = json.loads(requests.get('https://www.bitmex.com/api/v1/Insurance?start='+str(start)+'&count=500').text)
    return(cur)

fund_full = get_Ins(0)
#iter for number of days currently needed. In future may need to raise to 5 or more. 
for i in range (1,4):
    ins = get_Ins(500*i)
    fund_full.extend(ins)
insurance_fund = pd.DataFrame(fund_full)
insurance_fund.to_csv('MEX_Insurance.csv')

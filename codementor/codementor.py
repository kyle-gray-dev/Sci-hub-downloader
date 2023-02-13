import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

f = open('account01.txt')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
i = 0
count = len(data['hits'])
result = []
for x in data['hits']:
    # time.sleep(10)
    # # get codementor
    # url = "https://www.codementor.io/@" + x["username"]
    # response = requests.get(url)

    # soup = BeautifulSoup(response.content, 'html.parser')

    # link = soup.select_one('.linkedin-url')
    # if link is None:
    #     print(f"{i + 1}/{count}", x["username"], "There is no linkedin")  
    #     i += 1
    #     continue  

    # href = link["href"]
    # print(f"{i + 1}/{count}", x["username"], href)
    # x["linkedin"] = href

    result.append(x)
    # break

    i += 1


df = pd.DataFrame.from_dict(result)
df.to_excel("accounts1.xlsx")

    
  
# Closing file
f.close()
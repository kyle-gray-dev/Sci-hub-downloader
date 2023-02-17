import os
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        items = os.path.splitext(name)
        if items[1] != ".txt" or len(name) != len("account02-2018-04-01-07-01.txt"):
            continue;

        print(name)

        f = open(name)
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        # list
        i = 0
        count = len(data['hits'])
        result = []
        for x in data['hits']:
            time.sleep(1)
            # get codementor
            try:
                url = "https://www.codementor.io/@" + x["username"]
                response = requests.get(url)

                soup = BeautifulSoup(response.content, 'html.parser')

                link = soup.select_one('.linkedin-url')
                if link is None:
                    print(f"{i + 1}/{count}", x["username"], "There is no linkedin")  
                    i += 1
                    continue  

                href = link["href"]
                print(f"{i + 1}/{count}", x["username"], href)
                x["linkedin"] = href

                result.append(x)
                
            except:
                print("Network error")

            i += 1


        df = pd.DataFrame.from_dict(result)
        df.to_excel(f"{items[0]}.xlsx")
            
        
        # Closing file
        f.close()
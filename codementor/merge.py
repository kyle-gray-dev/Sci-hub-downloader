import os
import json
import pandas as pd

result = []

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        items = os.path.splitext(name)
        if items[1] != ".xlsx" or len(name) != len("account02-2018-04-01-07-01.xlsx"):
            continue

        print(name)

        df = pd.read_excel(name)
        for index, row in df.iterrows():            
            data = {}
            data["filename"] = name
            data["username"] = row["username"]
            data["linkedin"] = row["linkedin"]

            result.append(data)
            # break

# print(result)

df = pd.DataFrame.from_dict(result)
df.to_excel(f"total_new_codementors.xlsx")

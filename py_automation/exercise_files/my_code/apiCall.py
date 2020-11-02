# %%
import requests
import json
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '619659176709'}
response = requests.get(baseUrl, params=parameters)
print(response.url)

# %%
# Manage the content sent back from the interface of the website
content = response.content
# Use loads function that converts JSON documents into dictionaries
info = json.loads(content)
print(type(info))
print(info)

# %%
# Isolate item name and brand
item = info['items'] # Access items key of the dictionary, that has name and brand info
itemInfo = item[0] # Access first and only element of the dictionary value of the item
title = itemInfo['title'] # Grab dictionary value for the title key
brand = itemInfo['brand'] # Grab dictionary value for the brand key

# %%
print(title)
print(brand)
# %%

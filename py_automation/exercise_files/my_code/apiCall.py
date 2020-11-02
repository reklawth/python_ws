# %%
import requests

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '039800117274'}
response = requests.get(baseUrl, params=parameters)
print(response.url)

# %%

# %%
# Creating a request and parsing
import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# %%
# Isolate data
quotes = soup.find_all('span', class_='text') # Get quote (span tag, class text)
authors = soup.find_all('small', class_='author') # Get author (small tag, class author)
tags = soup.find_all('div', class_='tags') # Get tags for quote by author (div tag, class tags)
print(quotes)

# %%
# Loop to print each quote in quotes (identifed with 'text' tag)
for quote in quotes:
    print(quote.text)

# %%
# Loop to print quotes and authors
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags: # iterate through quote tags and print attributes
        print(quoteTag.text)
        
# %%

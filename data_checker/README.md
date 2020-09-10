# Web Scraper

## Notes:
- https://docs.scrapy.org/en/latest/index.html

- ```
  pipenv install --python python3.8 scrapy
  ```
- ```
  pipenv shell
  ```
- ```
  scrapy startproject data_checker .
  ```

- ```
  scrapy genspider dataset catalog.data.gov
  ```

- https://catalog.data.gov/dataset

- ```
  scrapy shell https://catalog.data.gov/dataset
  ```
  ```
  >>> response
<200 https://catalog.data.gov/dataset>
>>> len(response.css(".dataset-content"))
20
>>> dataset = response.css(".dataset-content")[0]
>>> dataset
<Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' dataset-content ')]" data='<div class="dataset-content">\n      \n...'>
>>> dataset.css("h3.dataset-heading > a::text")
[<Selector xpath="descendant-or-self::h3[@class and contains(concat(' ', normalize-space(@class), ' '), ' dataset-heading ')]/a/text()" data='U.S. Hourly Precipitation Data'>]
>>> dataset.css("h3.dataset-heading > a::text").get()
'U.S. Hourly Precipitation Data'
>>> dataset.css("h3.dataset-heading > a::attr(href)").get()
'/dataset/u-s-hourly-precipitation-data'
>>> dataset.css(".dataset.organization::text").get()
>>> dataset.css(".dataset-organization::text").get()
'National Oceanic and Atmospheric Administration, Department of Commerce —'
  ```

- ```
  scrapy crawl dataset
  ```
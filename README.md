#### HolySpider

#### Tools used:

- Scrapy: Python's robust web scrapping framework (that can
manage requests asynchronously, follow links and parse site
content)
- MongoDB: A scalable NoSQL db that stores data in JSON-
like format(to store scrapped data)

#### How HolySpider works:

- Extract data from the websites using Scrapy.
- Transform data (by cleaning or validating it).
- Load the transformed data into a database(MongoDB).

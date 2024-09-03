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

#### How To Use Holy Spider:

1. Find information about the site you want to get information from:

- Identify the specific elements that you want to scrape.
- Inspect the HTML to locate these elements.
- Gather the unique selectors for each piece of information that you want to scrape.

2. Preview the data with Scrapy Shell:

Open the shell and point it to the site that you want to scrape by using the `shell`
command followed by the site's URL:



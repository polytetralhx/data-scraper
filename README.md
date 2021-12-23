# data-scraper
I attempt to scrape data from Songwriter Universe, a website that includes a Directory of Record Labels from the United States, Canada and the United Kingdom, including both major and top independent companies.
To attempt this project, I made use of the Python libraries requests, bs4 (BeautifulSoup) to parse each page of the directory. Regex and inbuilt conditional expressions were used to extract the name, address, website and fax/phone numbers (wherever possible and not encrypted for security reasons). Pandas was also imported for usage to convert the information into a dataframe for geospatial analysis.
As the length of each list was different, I was unable to put the information together into a pandas dataframe and convert the information parsed into a dataset. Future commits may include trying to fix this mistake by editing small portions of the current code.
(23/12/2021)

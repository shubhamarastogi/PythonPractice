import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.nseindia.com/'
page = requests.get(url)
soup = bs(page.content,'html.parser')
print(soup)

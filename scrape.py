from requests import get
from  bs4 import BeautifulSoup

url  = 'https://www.nwslsoccer.com/stats?season=2018#players'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
container = html_soup.findAll('script')
print(container.script.script)
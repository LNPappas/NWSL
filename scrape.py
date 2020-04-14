from requests import get
from  bs4 import BeautifulSoup


url  = 'https://www.nwslsoccer.com/stats?season=2019#players'
source = get(url).text

soup = BeautifulSoup(source, 'lxml')
a = soup.find('div', attrs={'class': 'jsx-3685453796'})
# soup.find('div', attrs={'class': })
b = a.find('div', attrs={'class': 'jsx-3685453796 page-content-wrapper'})
c = b.find('div', attrs={'class': 'c-stats-nav-tabs'})
d = c.find_all('div', attrs={'class': 'c-tabbed-content jsx-548402753'})
# e = d.find('div', attrs={'class': "c-tabbed-content__tabs-wrapper jsx-548402753"})
f = d.find('div', attrs={'class': "jsx-2754883954 c-content-width-limiter"})

# g = f.find('div', attrs={'class': "jsx-"})
# h = g.find('div', attrs={'class': 'none'}) 
# y = x.find('div', attrs={'class': 'ReactVirtualized__Grid__innerScrollContainer'})
print(f)
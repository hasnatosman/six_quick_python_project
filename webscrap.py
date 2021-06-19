import requests
from bs4 import BeautifulSoup as bs

url = 'https://github.com/hasnatosman'
r = requests.get(url)
soup = bs(r.content, 'html.parser')

profile_image = soup.find('img',{'alt': 'Avatar'})['src']
print(profile_image)

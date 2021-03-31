import requests
from bs4 import BeautifulSoup
url = 'https://www.google.com/search?q=game+of+thrones&oq=game+of+thrones&aqs=chrome.0.69i59j46i433j0j69i60j69i65l3j69i60.2851j0j4&sourceid=chrome&ie=UTF-8'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("First four h2 tags from the webpage python.org.:")
print(soup.find_all('h2')[0:4])


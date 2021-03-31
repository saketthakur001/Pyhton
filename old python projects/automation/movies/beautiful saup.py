import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.google.com/search?q=game+of+thrones&oq=game+of+thrones&aqs=chrome.0.69i59j46i433j0j69i60j69i65l3j69i60.2851j0j4&sourceid=chrome&ie=UTF-8')
soup = bs.BeautifulSoup(sauce, 'lxml')
print(soup.find_all('p'))
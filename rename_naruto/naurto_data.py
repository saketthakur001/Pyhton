from bs4 import BeautifulSoup
from requests import get

season = 1
# f = open(r"C:\Users\saket\Desktop\rename\naruto"+str(season), 'x')


page = get('https://en.wikipedia.org/wiki/List_of_Naruto:_Shippuden_episodes')
soup = str(BeautifulSoup(page.content, 'html.parser'))
no = 1
while True:
    episode_lis = list(soup.split('class="summary" style="text-align:left">"'))
    episode = str(episode_lis[no])
    type(episode)

    episode = episode.split('"<br/>')[0]
    print(episode)
    no += 1
    # f.write(episode)
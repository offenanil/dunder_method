# web scraping for title

import requests
result = requests.get("http://www.example.com")
# print(type(result))
print(result.text)
import bs4
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
print(soup.select('title'))
print(soup.select('p'))
site_paragraph = soup.select('p')
print(site_paragraph[0].getText())

# web scraping for grabing class
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text, "lxml")
# print(soup)
print(soup.select('.toctext'))
# scrabing image

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.select('img')[0])
print(soup.select('.thumbimage'))
computer = soup.select('.thumbimage')[0]
print(computer['src'])
# <img src = "//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png">
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png")
# print(image_link.content)
f = open('my_computer_iamge.png', 'wb')
f.write(image_link.content)
f.close()
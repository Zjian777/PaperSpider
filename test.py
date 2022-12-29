import requests
from bs4 import BeautifulSoup

url = "https://www.x-mol.com/paper/search/q?option=coronavirus"
urlcode = requests.get(url)
soup = BeautifulSoup(urlcode.text,"lxml")
tag = soup.find_all('div',class_="it-bold space-bottom-m10")
print (tag)

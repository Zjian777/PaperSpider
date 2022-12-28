import requests
from bs4 import BeautifulSoup

url = "https://www.x-mol.com/paper/search/q?option=coronavirus"
urlcode = requests.get(url)
soup = BeautifulSoup(urlcode.text,"lxml")
tag = soup.find_all('div',class_="it-bold space-bottom-m10")
for i in tag:
	with open(file = "/root/code/output.txt",mode = 'a',encoding ='utf-8')as f:
		text = i.get_text().replace("\n","")
		f.write(text.strip())
		f.write("\n")
#This is the test text to see whether git is ok!

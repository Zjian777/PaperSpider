import requests
from bs4 import BeautifulSoup

url = 'https://www.1qxs.com/xs/67109.html'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
,"Cookies":"uid=ecfaeebc2d554289be163da60c23657d; Hm_lvt_dac3e73c19939b4f372cc10336edc17e=1672217645; read_history=67109:375,67601:232; Hm_lpvt_dac3e73c19939b4f372cc10336edc17e=1672219001'"
}
data = requests.get(url,headers = headers)
soup = BeautifulSoup(data.text,'lxml')
titles = soup.find_all('div',class_='line_1')
for i in titles:
	print(i.string)


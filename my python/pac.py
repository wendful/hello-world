import requests
from bs4 import BeautifulSoup

num = 1

for page in range(1,5):
	req = requests.get('http://www.qiushibaike.com/8hr/page/{}/'.format(page))
	html = req.text
	soup = BeautifulSoup(html,'lxml')		
		
	jokes = soup.select('a.contentHerf .content span')
	for joke in jokes:
		if joke.string is not None:
			joke_str = str(joke.string)
			joke_str = joke_str.replace('\n','')
			authors = soup.select('a h2')
			for author in authors:
				print('#{}:{}{}'.format(num,author.string,joke_str))
				num+= 1

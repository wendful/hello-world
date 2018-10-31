import requests
from bs4 import BeautifulSoup

def translate_num(salary):
	salary = salary.encode('utf_8')

	salary = salary.replace(b'\xee\xb3\x81',b'0')
	salary = salary.replace(b'\xee\xae\x9d',b'1')
	salary = salary.replace(b'\xef\xa2\xb0',b'2')
	salary = salary.replace(b'\xef\xa0\xb9',b'3')
	salary = salary.replace(b'\xee\xa2\x90',b'4')
	salary = salary.replace(b'\xee\xb4\xac',b'5')
	salary = salary.replace(b'\xee\x92\x99',b'6')
	salary = salary.replace(b'\xee\xb6\x94',b'7')
	salary = salary.replace(b'\xee\xbf\xa0',b'8')
	salary = salary.replace(b'\xee\x91\x9c',b'9')

	salary = salary.decode()

	return salary

	


def detail_page(url):
	detail_req = requests.get(url)
	detail_html = detail_req.text
	detail_soup = BeautifulSoup(detail_html,'lxml')

	job_name = detail_soup.select('.new_job_name')[0].string
	job_company = detail_soup.select('.job_com_name')[0].string
	job_money = translate_num(detail_soup.select('.job_money')[0].string)
	job_add = detail_soup.select('.job_position')[0].string

	print('{}:{}:{},{}'.format(job_name,job_company,job_money,job_add))

for page in range(1,5):
	req = requests.get('https://www.shixiseng.com/qita/{}'.format(page))
	html = req.text
	soup = BeautifulSoup(html,'lxml')
	for item in soup.select('a.name'):
		detail_url = item.get('href')
		detail_page('https://www.shixiseng.com'+detail_url)
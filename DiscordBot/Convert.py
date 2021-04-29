import requests
from bs4 import BeautifulSoup

class Convert:
	def __init__(self, header):
		self.header = header

	def convert(self, money):
		x = []
		page = requests.get('https://www.brd.ro/curs-valutar-si-dobanzi-de-referinta', self.header)
		soup = BeautifulSoup(page.content, 'html.parser')
		columns = soup.find_all('div', {'class':'col-xs-4'})
		for column in columns:
			x.append(column.get_text())
		x = x[3].split('\n')
		x = x[2].strip()
		x = float(x)
		return money * x

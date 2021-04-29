import requests
from bs4 import BeautifulSoup

class Dex:
	def __init__(self, header):
		self.header = header

	def dex(self, dex):
		page = requests.get(f'https://dexonline.ro/definitie/{dex}', self.header)
		soup = BeautifulSoup(page.content, 'html.parser')
		definitie = soup.find('span', {'class':'def'})
		return definitie.get_text()

	def __del__(self):
		print('Dex destroyed')


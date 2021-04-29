import requests
from bs4 import BeautifulSoup

class Weather:
	def __init__(self, header):
		self.header = header

	def weather(self):
		page = requests.get('https://www.accuweather.com/en/ro/bucharest/287430/current-weather/287430', headers = self.header)
		soup = BeautifulSoup(page.content, 'html.parser')
		temp = soup.find('div', {'class': 'temperature'}).get_text()
		temp = temp.strip()
		return f'{temp[:3]}C'

	def __del__(self):
		print('Weather destroyed')

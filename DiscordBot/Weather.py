import requests
from bs4 import BeautifulSoup

class Weather:
	def __init__(self, header):
		self.header = header
		self.page = requests.get('https://www.accuweather.com/en/ro/bucharest/287430/current-weather/287430', headers=self.header)
		self.soup = BeautifulSoup(self.page.content, 'html.parser')

	def weather(self):
		temp = self.soup.find('div', {'class': 'temperature'}).get_text()
		temp = temp.strip()
		return f'{temp[:3]}C'
	def current_weather(self, details=[]):
		temps = self.soup.findAll('div', {'class': 'detail-item spaced-content'})
		details = [temp.get_text().strip() for temp in temps]
		return '\n'.join(details)

	def __del__(self):
		print('Weather destroyed')


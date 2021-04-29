import requests

class Hentai:
	def __init__(self):
		self.response = requests.get('https://nhentai.net/random/')

	def random(self):
		return self.response.url

	def __del__(self):
		print('Hentai Destroyed')
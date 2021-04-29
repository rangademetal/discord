import datetime


class UTC:
	def __init__(self):
		pass 

	def utc_time(self):
		self.hour = datetime.datetime.utcnow().strftime("%H:%M:%S")
		self.minute = datetime.datetime.utcnow().strftime("%M")
		self.second = datetime.datetime.utcnow().strftime("%S")
		return 1

	def __del__(self):
		print('UTC destroyed')

utc = UTC()
print(utc.utc_time())
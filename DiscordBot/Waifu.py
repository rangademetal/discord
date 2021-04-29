import datetime
import random
import threading
import wikipedia 
import discord

from discord.ext import tasks, commands


class Waifu:
	def __init__(self):
		print('Chat Bot ONLINE!!!')

	def salutation(self):
		now = datetime.datetime.now()
		greetings = now.replace(hour=12, minute=0, second=0, microsecond=0)
		if now < greetings:
			return 'OHAYOU GOZAIMASU :hugging:'
		elif now > greetings:
			return 'KONBANWA :hugging:'

	def insult(self):
		return 'https://cdn.discordapp.com/attachments/761138834523291668/831204429612843018/hatsune.gif'

	def sad_face(self):
		return 'https://cdn.discordapp.com/attachments/761138834523291668/831246368768000060/hatsune_sad.gif'

	def sad(self):
		return 'https://cdn.discordapp.com/attachments/761138834523291668/831247257075974204/download.gif'

	def shy_kiss(self):
		return 'https://cdn.discordapp.com/attachments/831241845404467221/831548973097156638/miku_bJmXhq6r.gif'

	def cute(self):
		return 'https://cdn.discordapp.com/attachments/831241845404467221/831600742137200670/download.gif'

	def baka(self):
		return 'https://cdn.discordapp.com/attachments/831241845404467221/831604377903038554/download_2.gif'

	async def hello_everybody(self, client):
		channel = client.get_channel(831217157022416956)
		await channel.send(f'@everyone Hello')

	async def wikipedia(self, client, content):
		channel = client.get_channel(831217157022416956)
		embed=discord.Embed(title=content, description=f'{wikipedia.summary(content)}', color=0xFF5733)
		await channel.send(embed=embed)
import discord
import os
import asyncio
import random
import Database.Secret as secret
import DiscordBot.Minecraft as minecraft

# from DiscordBot.Lolapi import Lolapi
from DiscordBot.Convert import Convert
from DiscordBot.Dex import Dex
from DiscordBot.Waifu import Waifu
from DiscordBot.Weather import Weather
from Database.Connect import Connection
from MiningBot.Hentai import Hentai
from discord.ext import tasks, commands

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
db = Connection(secret.SERVER, secret.USERNAME, secret.PASSWORD, secret.DATABASE)
database = db.connect()
client = discord.Client()

waifu = Waifu()

# try:
#     status = Lolapi()
# except:
#     print('Update your API KEY')

@tasks.loop(minutes=60.0)
async def afk_destroyer():
    channel = client.get_channel(831217157022416956)
    await channel.send(f'{db.bot_afk(database)}')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    afk_destroyer.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'{message.author} -> {message.content}')
    checker = db.check_username(database, str(message.author))
    print(checker)
    if not checker:
        db.add_use(database, str(message.author))
        await message.channel.send(f'Hello {message.author}')
    else:
        print('In database')

    channels = ['nude']
    hatsune = 'hatsune-room'
   
    if str(message.channel) in channels:
        if message.content.startswith('porn'):
            picture = db.select_nude(database)
            picture = str(picture)
            await message.channel.send(picture)
    
    # HATSUNE ROOM COMMANDS
    if str(message.channel) in hatsune:
        if message.content.startswith('start minecraft server'):
            minecraft.start()
            await message.channel.send('Minecraft server is started')

        if message.content.startswith('stop minecraft server'):
            minecraft.stop()
            await message.channel.send('Minecraft server is stopped')

        if message.content.startswith('download minecraft'):
            await message.channel.send(minecraft.get_minecraft())

        if message.content.startswith('code'):
            code = message.content
            code = code.split(' ')
            code = code[-1]
            embed=discord.Embed(title=f'{db.select_function_title_by_id(database, code)}', description=f"{db.select_function_description_by_id(database, code)}", color=0xFF5733)
            await message.channel.send(embed=embed)
            await message.channel.send(f'```css\n{db.select_function_code_by_id(database, code)}```')

        if message.content.startswith('add photo'):
            link = message.content
            link = link.split(' ')
            link = link[-1]
            db.insert_hentai(database, link, '2021-04-21', 1, 2)
            await message.channel.send('New photo in my collection has added:smiling_face_with_3_hearts:! Thank you Senpai')
        if message.content.startswith('hentai'):
            picture = db.select_hentai(database)
            await message.channel.send(picture)        

        if message.content.startswith('nhentai'):
            hentai = Hentai()
            await message.channel.send(hentai.random())
            del hentai

        if client.user.mentioned_in(message):
            reaction='\U0001F44D'
            await message.channel.send(f'https://cdn.discordapp.com/attachments/831241845404467221/831569755147730944/hatsun_miku_shy_kiss.gif')
            await message.channel.send(f'{message.author.mention} Senpai')
            await message.add_reaction(emoji=reaction)

        if message.content.startswith('lust'):
            author = str(message.author)
            username = db.status_lust(database, author)
            embed=discord.Embed(title="Lust", description=f"{author} have {username} lust points! Keep it up oni-chan:kissing_heart:.", color=0xFF5733)
            await message.channel.send(embed=embed)

        if message.content.startswith('dex'):
            dex = Dex(header)
            word = message.content
            word = word.split(' ')
            word = word[-1]

            checker = db.check_dex(database, word)
            definition = dex.dex(word)
            
            if checker == True:
                embed = discord.Embed(title=word, description=definition, color=0xFF5733)
                await message.channel.send(embed=embed)
            else:
                
                db.dex(database, word, definition)
                embed = discord.Embed(title=word, description=definition, color=0xFF5733)
                await message.channel.send(embed=embed)
                await message.channel.send(f'Thank you for teaching me the new word {word}, Senpai:hugging:.')
            del dex
        
        if message.content.startswith('weather'):
            weather = Weather(header)
            await message.channel.send(f'The weather in Bucharest is {weather.weather()}')
            del weather
        if message.content.startswith('currently weather'):
            weather = Weather(header)
            embed = discord.Embed(title=f'Details weather', description=weather.current_weather(), color=0xFF5733)
            await message.channel.send(embed=embed)
            del weather
        
        if message.content.startswith('how many words you know?'):
            words = db.count_dex(database)
            await message.channel.send(f"In this moment I know {words} words. Thank you to have care about me. I am happy to learn more new things from you. Please fill me with new knowledge")

        patterns = message.content
        checker = db.patterns_keys(database, patterns)
        checker = str(checker)

        if message.content == checker:
            msg = db.general_status(database, checker)
            author = str(message.author)
            point = db.get_point_lust(database, author)
            username = db.get_id_user(database, author)
            point += 1
            if random.randint(0, 100) > 50:
                db.update_points(database, point, username)
            await message.channel.send(msg)
            await message.channel.send(f'{message.author.mention}')
            
    if message.content.startswith('time'):
        await message.content.send(datetime.datetime.utcnow().strftime("%H:%M:%S"))

    if message.content.startswith('show nude'):
        picture = db.show_selected(database)
        await message.channel.send(f'{picture} nude pictures')

    if message.content.startswith('help'):
        picture = db.show_command(database)
        await message.channel.send(f'{picture}')

    if message.content.startswith('status'):
        if message.content != 'status':
            username = message.content.replace('status', '')
            username = username.strip()
            await message.channel.send(status.status(username))
        else:
            username = db.status_lol(database, str(message.author))
            await message.channel.send(status.status(username))

    if message.content.startswith('convert'):
        convertor = Convert(header)
        money = message.content
        money = money.split(' ')
        money = money[-1]
        money = int(money)
        await message.channel.send(f'{money} EURO -> {convertor.convert(money)} RON')
        
client.run(secret.TOKEN) 
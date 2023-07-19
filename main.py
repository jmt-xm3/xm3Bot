import os
import shutil


currentDirectory = os.getcwd()
tempDirectory = os.path.join(currentDirectory, 'temp')


def clearTempDirectory():
    shutil.rmtree(tempDirectory)
    os.mkdir("temp")



# example bot figure out what to do later
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def test(ctx):
    print('nice')
    pass

client.run('MTEyOTE5MDk3MTc5NjYzNTY0OA.GRSyl9.HIHgEWFNQ-VTt1MiyRYZDF41iutxWUAussL-So') 

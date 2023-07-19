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

    if message.content.startswith('free tay k'):
        await message.channel.send(file=discord.File('/home/jonan0/Documents/GitHub/xm3Bot/23027.zip'))

client.run('MTEyOTE5MDk3MTc5NjYzNTY0OA.GRSyl9.HIHgEWFNQ-VTt1MiyRYZDF41iutxWUAussL-So') 

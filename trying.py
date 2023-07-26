# help me

import discord
from discord.ext import commands
from liveryClasses import ACCLivery

with open('token.txt', 'r') as f:
    token = f.read()


def hexToTuple(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print('free tay k 47')
    print('------')

car1 = ACCLivery()
car1.setDazzleTopColour(hexToTuple('1E1E1E'))
car1.setDazzleBottomColour(hexToTuple('b57ebf'))
car1.setBaseColour(300)
car1.setBaseMaterialId(2)
car1.setCarModelType(20)
car1.setFolderName('JMT774')
car1.setInGameName('JMT')
car1.setRaceNumber(774)
car1.zipCar()
print(car1.getZipPath())

@bot.command()
async def xm3(ctx):
    await ctx.send(file=discord.File(car1.getZipPath()))

bot.run(token)
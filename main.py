import random
import discord
import os
import shutil
import datetime
from liveryClasses import accCarModels, ACCLivery
from discord.ext import commands


with open('token.txt','r') as f:
    token = f.read()
    

currentDirectory = os.getcwd()
tempDirectory = os.path.join(currentDirectory, 'temp')
newCarLivery = ACCLivery()
startTime = datetime.datetime.now()
materials = [{'key': 'Glossy', 'value': 0}, {'key': 'Matte', 'value': 1}, {'key': 'Satin', 'value': 2}, {
    'key': 'Satin Metallic', 'value': 3}, {'key': 'Metallic', 'value': 4}, {'key': 'Glossy', 'Chrome': 5}, {'key': 'Clear Chrome', 'value': 6}]
cars = [{'key': 'AMR V12 Vantage GT3', 'value': 12}, {'key': 'AMR V8 Vantage', 'value': 20}, {'key': 'Audi R8 LMS Evo', 'value': 19}, {'key': 'Audi R8 LMS GT3 Evo 2', 'value': 31}, {'key': 'Audi R8 LMS', 'value': 3}, {'key': 'BMW M4 GT3', 'value': 30}, {'key': 'BMW M6 GT3', 'value': 7}, {'key': 'Bentley Continental GT3 2015', 'value': 11}, {'key': 'Bentley Continental GT3 2018', 'value': 8}, {'key': 'Emil Frey Jaguar G3', 'value': 14}, {'key': 'Ferrari 296 GT3', 'value': 32}, {'key': 'Ferrari 488 GT3 Evo', 'value': 24}, {'key': 'Ferrari 488 GT3', 'value': 2}, {'key': 'Honda NSX GT3 Evo', 'value': 21}, {'key': 'Honda NSX GT3', 'value': 17}, {
    'key': 'Lamborghini Huracán GT3 Evo', 'value': 16}, {'key': 'Lamborghini Huracán GT3 EVO2', 'value': 33}, {'key': 'Lamborghini Huracán GT3', 'value': 4}, {'key': 'Lexus RC F GT3', 'value': 15}, {'key': 'McLaren 650S GT3', 'value': 5}, {'key': 'McLaren 720S GT3', 'value': 22}, {'key': 'McLaren 720S GT3 EVO', 'value': 35}, {'key': 'Mercedes-AMG GT3', 'value': 1}, {'key': 'Mercedes-AMG GT3 Evo', 'value': 25}, {'key': 'Nissan GT-R Nismo GT3 2015', 'value': 10}, {'key': 'Nissan GT-R Nismo GT3 2018', 'value': 6}, {'key': 'Porsche 991 GT3 R', 'value': 0}, {'key': 'Porsche 991 II GT3 R', 'value': 23}, {'key': 'Porsche 992 GT3 R', 'value': 34}, {'key': 'Reiter Engineering R-EX GT3', 'value': 13}]
available = []
for model in accCarModels:
    available.append(model['carModelType'])

for car in cars:
    if car['value'] not in available:
        cars.remove(car)
        
        
def clearTempDirectory():
    shutil.rmtree(tempDirectory)
    os.mkdir("temp")


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('hello  world')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} synced')
    except Exception as e:
        print(e)

@bot.tree.command(name='xm3time')
async def xm3TIme(interaction:discord.Interaction):
    await interaction.response.send_message(f"{startTime} innit")
    
@bot.tree.command(name="revsport")
@discord.app_commands.describe(car="figure out later")
async def revsport(interaction:discord.Interaction, car:str):
    await interaction.response.send_message(f"{interaction.user.name} wants: {str}")


bot.run(token)

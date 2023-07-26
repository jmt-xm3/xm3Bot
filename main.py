import random
import discord
import os
import shutil
import datetime
from liveryClasses import accCarModels, ACCLivery
from discord.ext import commands


with open('token.txt', 'r') as f:
    token = f.read()


def hexToTuple(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


currentDirectory = os.getcwd()
tempDirectory = os.path.join(currentDirectory, 'temp')
startTime = datetime.datetime.now()
materials = [{'key': 'Glossy', 'value': 0}, {'key': 'Matte', 'value': 1}, {'key': 'Satin', 'value': 2}, {
    'key': 'Satin Metallic', 'value': 3}, {'key': 'Metallic', 'value': 4}, {'key': 'Chrome', 'value': 5}, {'key': 'Clear Chrome', 'value': 6}]
cars = [{'key': 'AMR V12 Vantage GT3', 'value': 12}, {'key': 'AMR V8 Vantage', 'value': 20}, {'key': 'Audi R8 LMS Evo', 'value': 19}, {'key': 'Audi R8 LMS GT3 Evo 2', 'value': 31}, {'key': 'Audi R8 LMS', 'value': 3}, {'key': 'BMW M4 GT3', 'value': 30}, {'key': 'BMW M6 GT3', 'value': 7}, {'key': 'Bentley Continental GT3 2015', 'value': 11}, {'key': 'Bentley Continental GT3 2018', 'value': 8}, {'key': 'Emil Frey Jaguar G3', 'value': 14}, {'key': 'Ferrari 296 GT3', 'value': 32}, {'key': 'Ferrari 488 GT3 Evo', 'value': 24}, {'key': 'Ferrari 488 GT3', 'value': 2}, {'key': 'Honda NSX GT3 Evo', 'value': 21}, {'key': 'Honda NSX GT3', 'value': 17}, {
    'key': 'Lamborghini Huracán GT3 Evo', 'value': 16}, {'key': 'Lamborghini Huracán GT3 EVO2', 'value': 33}, {'key': 'Lamborghini Huracán GT3', 'value': 4}, {'key': 'Lexus RC F GT3', 'value': 15}, {'key': 'McLaren 650S GT3', 'value': 5}, {'key': 'McLaren 720S GT3', 'value': 22}, {'key': 'McLaren 720S GT3 EVO', 'value': 35}, {'key': 'Mercedes-AMG GT3', 'value': 1}, {'key': 'Mercedes-AMG GT3 Evo', 'value': 25}, {'key': 'Nissan GT-R Nismo GT3 2015', 'value': 10}, {'key': 'Nissan GT-R Nismo GT3 2018', 'value': 6}, {'key': 'Porsche 991 GT3 R', 'value': 0}, {'key': 'Porsche 991 II GT3 R', 'value': 23}, {'key': 'Porsche 992 GT3 R', 'value': 34}, {'key': 'Reiter Engineering R-EX GT3', 'value': 13}]
available = []
for model in accCarModels:
    available.append(model['carModelType'])
for car in cars:
    if car['value'] not in available:
        cars.remove(car)
availableCars = []
finishes = []
for car in cars:
    availableCars.append(discord.app_commands.Choice(
        name=car['key'], value=car['value']))

for finish in materials:
    finishes.append(discord.app_commands.Choice(
        name=finish['key'], value=finish['value']))


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
async def xm3time(interaction: discord.Interaction):
    await interaction.response.send_message(f"{startTime} innit")


@bot.tree.command(name='xm3sync')
async def xm3sync(interaction: discord.Interaction):
    try:
        synced = await bot.tree.sync()
        await interaction.response.send_message(f'Synced {len(synced)} synced')
        print(f'Synced {len(synced)} synced')
    except Exception as e:
        print(e)


@bot.tree.command(name='xm3die')
async def xm3TIme(interaction: discord.Interaction):
    await interaction.response.send_message("zamn")
    quit()


@bot.tree.command(name="revsport")
@discord.app_commands.describe(car="Car", base_colour='Base colour of car', finish='Finish of base colour', dazzle1='Hex code of top Dazzle', dazzle2='Hex code of bottom Dazzle')
@discord.app_commands.choices(car=availableCars)
@discord.app_commands.choices(finish=finishes)
async def revsport(interaction: discord.Interaction, car: discord.app_commands.Choice[int], finish: discord.app_commands.Choice[int], base_colour: int, dazzle1: str, dazzle2: str):
    try:
        dazzle1rgb = hexToTuple(dazzle1)
        dazzle2rgb = hexToTuple(dazzle2)
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Input a valid hex code", ephemeral=True)
        return
    try:
        if 0 < base_colour <= 359 or 500 <= base_colour <= 532:
            pass
        else:
            await interaction.response.send_message(f"Input a valid ACC colour", ephemeral=True)
            return
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Input a valid hex code", ephemeral=True)
        return

    new = ACCLivery()
    new.setCarModelType(car.value)
    new.setBaseColour(base_colour)
    new.setBaseMaterialId(finish.value)
    new.setDazzleTopColour(dazzle1rgb)
    new.setDazzleBottomColour(dazzle2rgb)
    new.zipCar()
    await interaction.response.send_message(f'Here is your new{car.value} livery',file=new.zipPath)    


bot.run(token)

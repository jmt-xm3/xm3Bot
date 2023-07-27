import asyncio
import discord
import os
import shutil
import datetime
from liveryClasses import accCarModels, ACCLivery
from discord.ext import commands

with open('token.txt', 'r') as f:
    token = f.read()


def hexToTuple(hexadecimal):
    return tuple(int(hexadecimal[i:i + 2], 16) for i in (0, 2, 4))


currentDirectory = os.getcwd()
tempDirectory = os.path.join(currentDirectory, 'temp')
startTime = datetime.datetime.now()
materials = [{'key': 'Glossy', 'value': 0}, {'key': 'Matte', 'value': 1}, {'key': 'Satin', 'value': 2}, {
    'key': 'Satin Metallic', 'value': 3}, {'key': 'Metallic', 'value': 4}, {'key': 'Chrome', 'value': 5},
             {'key': 'Clear Chrome', 'value': 6}]
cars = [
    {'key': 'AMR V12 Vantage GT3', 'value': 12},
    {'key': 'AMR V8 Vantage', 'value': 20},
    {'key': 'Audi R8 LMS Evo', 'value': 19},
    {'key': 'Audi R8 LMS GT3 Evo 2', 'value': 31},
    {'key': 'Audi R8 LMS', 'value': 3},
    {'key': 'BMW M4 GT3', 'value': 30},
    {'key': 'BMW M6 GT3', 'value': 7},
    {'key': 'Bentley Continental GT3 2015', 'value': 11},
    {'key': 'Bentley Continental GT3 2018', 'value': 8},
    {'key': 'Emil Frey Jaguar G3', 'value': 14},
    {'key': 'Ferrari 296 GT3', 'value': 32},
    {'key': 'Ferrari 488 GT3 Evo', 'value': 24},
    {'key': 'Ferrari 488 GT3', 'value': 2},
    {'key': 'Honda NSX GT3 Evo', 'value': 21},
    {'key': 'Honda NSX GT3', 'value': 17},
    {'key': 'Lamborghini Huracán GT3 Evo', 'value': 16},
    {'key': 'Lamborghini Huracán GT3 EVO2', 'value': 33},
    {'key': 'Lamborghini Huracán GT3', 'value': 4},
    {'key': 'Lexus RC F GT3', 'value': 15},
    {'key': 'McLaren 650S GT3', 'value': 5},
    {'key': 'McLaren 720S GT3', 'value': 22},
    {'key': 'McLaren 720S GT3 EVO', 'value': 35},
    {'key': 'Mercedes-AMG GT3', 'value': 1},
    {'key': 'Mercedes-AMG GT3 Evo', 'value': 25},
    {'key': 'Nissan GT-R Nismo GT3 2015', 'value': 10},
    {'key': 'Nissan GT-R Nismo GT3 2018', 'value': 6},
    {'key': 'Porsche 991 GT3 R', 'value': 0},
    {'key': 'Porsche 991 II GT3 R', 'value': 23},
    {'key': 'Porsche 992 GT3 R', 'value': 34},
    {'key': 'Reiter Engineering R-EX GT3', 'value': 13},
    {'key': 'Alpine A110 GT4', 'value': 50},
    {'key': 'Aston Martin Vantage GT4', 'value': 51},
    {'key': 'Audi R8 LMS GT4', 'value': 52},
    {'key': 'BMW M4 GT4', 'value': 53},
    {'key': 'Chevrolet Camaro GT4', 'value': 55},
    {'key': 'Ginetta G55 GT4', 'value': 56},
    {'key': 'KTM X-Bow GT4', 'value': 57},
    {'key': 'Maserati MC GT4', 'value': 58},
    {'key': 'McLaren 570S GT4', 'value': 59},
    {'key': 'Mercedes AMG GT4', 'value': 60},
    {'key': 'Porsche 718 Cayman GT4 Clubsport', 'value': 61},
    {'key': 'Ferrari 488 Challenge Evo', 'value': 26},
    {'key': 'Lamborghini Huracan SuperTrofeo', 'value': 18},
    {'key': 'Lamborghini Huracán SuperTrofeo EVO2', 'value': 29},
    {'key': 'Porsche 991 II GT3 Cup', 'value': 9},
    {'key': 'Porsche 992 GT3 Cup', 'value': 28},
    {'key': 'BMW M2 Club Sport Racing', 'value': 27},
]
available = []
for model in accCarModels:
    for c in cars:
        if model['carModelType'] == c['value']:
            available.append(c)
availableCars = []
finishes = []
for c in available:
    availableCars.append(discord.app_commands.Choice(
        name=c['key'], value=c['value']))

for finish in materials:
    finishes.append(discord.app_commands.Choice(
        name=finish['key'], value=finish['value']))


def clearTempDirectory():
    shutil.rmtree(tempDirectory)
    os.mkdir("temp")


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print('free tay k 47')
    print('------')


@bot.tree.command(name='xm3time')
async def xm3time(interaction: discord.Interaction):
    currentTime = datetime.now()
    timeDifference = currentTime - startTime
    days = timeDifference.days
    hours, remainder = divmod(timeDifference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    startTimeFormatted = startTime.strftime("%d/%m/%Y")
    await interaction.response.send_message(
        f"xm3 bot has been alive since {startTimeFormatted} for: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")


@bot.tree.command(name="xm3sync")
async def xm3sync(interaction: discord.Interaction):
    try:
        synced = await bot.tree.sync()
        await interaction.response.send_message(f'Synced {len(synced)} commands')
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(e)


@bot.tree.command(name="xm3credits")
async def xm3credits(interaction: discord.Interaction):
    await interaction.response.send_message(
        f'credit to Marley (brexite) for making basically every one of these liveries. shout out me (sonywh1000xm3) '
        f'for making the bot and the porsche 992 and lambo evo 2 ')


@bot.tree.command(name="xm3die")
async def xm3die(interaction: discord.Interaction):
    await interaction.response.send_message("zamn")
    print('rip bot')
    quit()


@bot.tree.command(name="xm3help")
async def xm3help(interaction: discord.Interaction):
    await interaction.response.send_message("If you're struggling to put in a valid hex code it will look like "
                                            "'111FFF' each digit can be 0-9 or A-F. Also here are all the colours in "
                                            "acc if you need help with "
                                            "base_colour:", file=discord.File('accColours.png'), ephemeral=True)


@bot.tree.command(name="revsport")
@discord.app_commands.describe(car="Car model in ACC", race_number="Your race number", base_colour="Base colour of car",
                               finish="Finish for the base colour", dazzle1='Hex code of top dazzle',
                               dazzle2='Hex code of bottom dazzle')
@discord.app_commands.choices(car=availableCars)
@discord.app_commands.choices(finish=finishes)
async def revsport(interaction: discord.Interaction, car: discord.app_commands.Choice[int], race_number: int,
                   finish: discord.app_commands.Choice[int], base_colour: int, dazzle1: str, dazzle2: str):
    try:
        dazzle1rgb = hexToTuple(dazzle1)
        dazzle2rgb = hexToTuple(dazzle2)
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Give me a valid hex code /xm3help", ephemeral=True)
        return
    try:
        if 0 < base_colour <= 359 or 500 <= base_colour <= 532:
            pass
        else:
            await interaction.response.send_message(f"Give me a valid ACC Colour (1-359 and 500-532), try /xm3help",
                                                    ephemeral=True)
            return
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Give me a valid ACC Colour (1-359 and 500-532), try /xm3help",
                                                ephemeral=True)
        return

    try:
        if 0 <= race_number <= 999:
            pass
        else:
            await interaction.response.send_message(f"Give me a valid race number (0-999)", ephemeral=True)
            return
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Give me a valid race number (0-999)", ephemeral=True)
        return
    car1 = ACCLivery()
    car1.setDazzleTopColour(dazzle1rgb)
    car1.setDazzleBottomColour(dazzle2rgb)
    car1.setBaseColour(base_colour)
    car1.setBaseMaterialId(finish.value)
    car1.setCarModelType(car.value)
    car1.setFolderName(car1.liveryID)
    car1.setInGameName(car1.liveryID)
    car1.setRaceNumber(race_number)
    await interaction.response.defer(ephemeral=True)
    car1.createDazzle()
    car1.createJsonFile()
    await interaction.followup.send('art takes time mate')
    car1.zipCar()
    print(car1.getZipPath())
    await interaction.followup.send(content=f'Here is your new {car.name} livery, before sharing this I would '
                                            f'recommend changing the team name, the json name and playing around with'
                                            f' auxilery lights and rim colours. Due limitations with ACC you will '
                                            f'also need to load a track with the livery to generate the dds files',
                                    file=discord.File(car1.getZipPath()))


bot.run(token)

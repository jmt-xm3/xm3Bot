import asyncio
import discord
import os
import shutil
import datetime
import sqlite3
from liveryClasses import accCarModels, ACCLivery, iRacingLivery, iracingCars, iracingCars1
from discord.ext import commands, tasks

con = sqlite3.connect('preferences.db')
curs = con.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS user
            (id INTEGER PRIMARY KEY, 
            livery_name varchar(100) NOT NULL,
            race_number INT,
            finish INT,
            base_colour_acc INT NOT NULL,
            base_colour varchar(6) NOT NULL,
            dazzle1 varchar(6) NOT NULL, 
            dazzle2 varchar(6) NOT NULL)""")
con.commit()
con.close()

with open('token.txt', 'r') as f:
    token = f.read()


def hexToTuple(hexadecimal):
    if hexadecimal.startswith('#'):
        hexadecimal = hexadecimal[1:]
    return tuple(int(hexadecimal[i:i + 2], 16) for i in (0, 2, 4))


def is_valid_folder_name(folder_name):
    invalid_chars_windows = '<>:"/\\|?*'
    invalid_chars_unix = '/'
    if not folder_name.strip():
        return False
    if os.name == 'nt':
        invalid_chars = invalid_chars_windows
    else:
        invalid_chars = invalid_chars_unix
    if any(char in invalid_chars for char in folder_name):
        return False
    if os.name == 'nt':
        reserved_names = {'CON', 'PRN', 'AUX', 'NUL'}
        reserved_names.update('COM{}'.format(i) for i in range(1, 10))
        reserved_names.update('LPT{}'.format(i) for i in range(1, 10))
        if folder_name.upper() in reserved_names:
            return False

    # The folder name is valid
    return True


blacklist = [238400056942657538,]
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
accCars = []
sorted_data = sorted(available, key=lambda x: x['key'])
for c in sorted_data:
    accCars.append(discord.app_commands.Choice(
        name=c['key'], value=c['value']))
finishes = []
for f in materials:
    finishes.append(discord.app_commands.Choice(
        name=f['key'], value=f['value']))
iracingChoices = []
sorted_iracing = sorted(iracingCars, key=lambda x: x['key'])
for i in sorted_iracing:
    iracingChoices.append(discord.app_commands.Choice(
        name=i['key'], value=i['value']))

iracingChoices1 = []
sorted_iracing = sorted(iracingCars1, key=lambda x: x['key'])
for i in sorted_iracing:
    iracingChoices1.append(discord.app_commands.Choice(
        name=i['key'], value=i['value']))

allCars = accCars + iracingChoices  # I am paying for my awful variable names

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print('free tay k 47')
    print('------')
    clearTempDirectory.start()


@tasks.loop(seconds=43200)
async def clearTempDirectory():
    print('clearing temp every 12 hours')
    await asyncio.sleep(1)
    shutil.rmtree(tempDirectory)
    os.mkdir("temp")
    print('temp is cleared')


@bot.tree.command(name='xm3time')
async def xm3time(interaction: discord.Interaction):
    currentTime = datetime.datetime.now()
    timeDifference = currentTime - startTime
    days = timeDifference.days
    hours, remainder = divmod(timeDifference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    startTimeFormatted = startTime.strftime("%d/%m/%Y")
    await interaction.response.send_message(
        f"xm3 bot has been alive since {startTimeFormatted} for: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")


@bot.tree.command(name="xm3sync")
async def xm3sync(interaction: discord.Interaction):
    if interaction.user.id == 412281276922462219:
        try:
            synced = await bot.tree.sync()
            await interaction.response.send_message(f'Synced {len(synced)} commands', ephemeral=True)
            print(f'Synced {len(synced)} commands')
        except Exception as e:
            print(e)
    else:
        await interaction.response.send_message(f'not permitted to do that', ephemeral=True)
        print(interaction.user.id)


@bot.tree.command(name="xm3credits")
async def xm3credits(interaction: discord.Interaction):
    await interaction.response.send_message(
        f'Credit to Marley (brexite) for making the original REVSPORT INTERNATIONAL livery, Pete (Simber1) for the liveries for NASCAR Trucks and Jack for allowing me to modify his Porsche 992 for the this bot.', ephemeral=True)


@bot.tree.command(name="xm3help")
async def xm3help(interaction: discord.Interaction):
    await interaction.response.send_message(
        "If you're struggling to put in a valid hex code it will look like 'AFC193', do not add a hashtag, each digit can be 0-9 or A-F. Also here are all the colours in acc if you need help with base_colour:",
        file=discord.File('accColours.png'), ephemeral=True)


@bot.tree.command(name="reviracing", description='Standard REVSPORT IRacing livery')
@discord.app_commands.describe(car="Car model in Iracing",
                               base_colour="Hex code of base paint of car (F1F1F1 as an example)",
                               dazzle1='Hex code of top dazzle (F1F1F1 as an example)',
                               dazzle2='Hex code of bottom dazzle (F1F1F1 as an example)')
@discord.app_commands.choices(car=iracingChoices)
async def revsportIRacing(interaction: discord.Interaction, car: discord.app_commands.Choice[int], base_colour: str,
                          dazzle1: str, dazzle2: str):
    if interaction.user.id in blacklist:
        await interaction.response.send_message(f"You are not permitted to do that", ephemeral=True)
    else:
        try:
            daze1 = hexToTuple(dazzle1)
            daze2 = hexToTuple(dazzle2)
            base = hexToTuple(base_colour)
        except Exception as e:
            print(e)
            await interaction.response.send_message(
                f"Give me a valid hex code", ephemeral=True)
            return
        car1 = iRacingLivery()
        for x in iracingCars:
            if x["value"] == car.value:
                chosen = x
                break
        await interaction.response.defer()
        car1.set_car(chosen['file'])
        car1.set_dazzle1(daze1)
        car1.set_dazzle2(daze2)
        car1.set_base_colour(base)
        await interaction.followup.send('finishing touches...')
        specMap, carPath = car1.create_livery()
        await interaction.followup.send(
            content=f"Here is your {chosen['key']}, upload it on trading paints under 'Just Me' ",
            files=[discord.File(specMap), discord.File(carPath)])


@bot.tree.command(name="reviracing2", description='Standard REVSPORT IRacing livery (car set 2)')
@discord.app_commands.describe(car="Car model in IRacing",
                               base_colour="Hex code of base paint of car (F1F1F1 as an example)",
                               dazzle1='Hex code of top dazzle (F1F1F1 as an example)',
                               dazzle2='Hex code of bottom dazzle (F1F1F1 as an example)')
@discord.app_commands.choices(car=iracingChoices1)
async def revsportIRacing(interaction: discord.Interaction, car: discord.app_commands.Choice[int], base_colour: str,
                          dazzle1: str, dazzle2: str):
    if interaction.user.id in blacklist:
        await interaction.response.send_message(f"You are not permitted to do that", ephemeral=True)
    else:
        try:
            daze1 = hexToTuple(dazzle1)
            daze2 = hexToTuple(dazzle2)
            base = hexToTuple(base_colour)
        except Exception as e:
            print(e)
            await interaction.response.send_message(
                f"Give me a valid hex code", ephemeral=True)
            return
        car1 = iRacingLivery()
        for x in iracingCars1:
            if x["value"] == car.value:
                chosen = x
                break
        await interaction.response.defer()
        car1.set_car(chosen['file'])
        car1.set_dazzle1(daze1)
        car1.set_dazzle2(daze2)
        car1.set_base_colour(base)
        await interaction.followup.send('finishing touches...')
        specMap, carPath = car1.create_livery()
        await interaction.followup.send(
            content=f"Here is your {chosen['key']}, upload it on trading paints under 'Just Me' ",
            files=[discord.File(specMap), discord.File(carPath)])


@bot.tree.command(name="carpreferences", description='Set your preferences for your car to use the /mycar command')
@discord.app_commands.describe(livery_name="In-game and folder name for livery in ACC",
                               race_number="Your race number",
                               base_colour_acc="Base colour of car (number in ACC) use /xm3help if unsure",
                               base_colour="Hex code for base colour in IRacing (F1F1F1 as an example)",
                               finish="Finish for the base colour in acc",
                               dazzle1='Hex code of top dazzle (F1F1F1 as an example)',
                               dazzle2='Hex code of bottom dazzle (F1F1F1 as an example)')
@discord.app_commands.choices(finish=finishes)
async def carPreferences(interaction: discord.Interaction, livery_name: str,
                         race_number: int,
                         finish: discord.app_commands.Choice[int], base_colour_acc: int, base_colour: str, dazzle1: str,
                         dazzle2: str):
    if interaction.user.id in blacklist:
        await interaction.response.send_message(f"You are not permitted to do that", ephemeral=True)
    if is_valid_folder_name(livery_name):
        pass
    else:
        await interaction.response.send_message(f"Give me a valid name", ephemeral=True)
    try:
        hexToTuple(dazzle1)
        hexToTuple(dazzle2)
        hexToTuple(base_colour)
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Give me a valid hex code",
                                                ephemeral=True)
        return
    try:
        if 0 < base_colour_acc <= 359 or 500 <= base_colour_acc <= 532:
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
    else:
        conn = sqlite3.connect('preferences.db')
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO user VALUES(?,?,?,?,?,?,?,?)", (interaction.user.id,
                                                                            livery_name, race_number, finish.value,
                                                                            base_colour_acc, base_colour, dazzle1,
                                                                            dazzle2))
        conn.commit()
        conn.close()
        await interaction.response.send_message(f"Preference set", ephemeral=True)


@bot.tree.command(name="revacc", description='Standard REVSPORT Assetto Corsa Competizione livery')
@discord.app_commands.describe(livery_name="In-game and folder name for livery (in-game name can be changed after)",
                               car="Car model in ACC",
                               race_number="Your race number", base_colour="Base colour of car (number in ACC)",
                               finish="Finish for the base colour ",
                               dazzle1='Hex code of top dazzle (F1F1F1 as an example)',
                               dazzle2='Hex code of bottom dazzle (F1F1F1 as an example)')
@discord.app_commands.choices(car=accCars)
@discord.app_commands.choices(finish=finishes)
async def revsportACC(interaction: discord.Interaction, livery_name: str, car: discord.app_commands.Choice[int],
                      race_number: int,
                      finish: discord.app_commands.Choice[int], base_colour: int, dazzle1: str, dazzle2: str):
    if interaction.user.id in blacklist:
        await interaction.response.send_message(f"You are not permitted to do that", ephemeral=True)
    else:
        pass
    if is_valid_folder_name(livery_name):
        pass
    else:
        await interaction.response.send_message(f"Give me a valid name", ephemeral=True)
    try:
        dazzle1rgb = hexToTuple(dazzle1)
        dazzle2rgb = hexToTuple(dazzle2)
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Give me a valid hex code",
                                                ephemeral=True)
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
    car1.setFolderName(livery_name)
    car1.setInGameName(livery_name)
    car1.setRaceNumber(race_number)
    await interaction.response.defer()
    car1.createDazzle()
    car1.createJsonFile()
    await interaction.followup.send('finishing touches...')
    car1.zipCar()
    print(car1.getZipPath())
    await interaction.followup.send(
        content=f"Here is your {car.name}, you should probably change the name of the json file",
        file=discord.File(car1.getZipPath()))


@bot.tree.command(name="myrevacc", description='ACC Revsport Livery based on preferences set in /carpreferences')
@discord.app_commands.describe(car="Car model in ACC/iRacing")
@discord.app_commands.choices(car=accCars)
async def myCar(interaction: discord.Interaction, car: discord.app_commands.Choice[int]):
    if interaction.user.id not in blacklist:
        try:
            conn = sqlite3.connect("preferences.db")
            cur = conn.cursor()
            user_id = int(interaction.user.id)
            cur.execute("SELECT * FROM user WHERE id = ?", (user_id,))
            user_data = cur.fetchone()  # Assuming you're expecting one row
            if user_data:
                column_names = [description[0]
                                for description in cur.description]
                userPref = dict(zip(column_names, user_data))
                folderName = userPref['livery_name'] + '' + car.name
                daz1 = hexToTuple(userPref['dazzle1'])
                daz2 = hexToTuple(userPref['dazzle2'])
                car1 = ACCLivery()
                car1.setDazzleTopColour(daz1)
                car1.setDazzleBottomColour(daz2)
                car1.setBaseColour(userPref['base_colour_acc'])
                car1.setBaseMaterialId(userPref['finish'])
                car1.setCarModelType(car.value)
                car1.setFolderName(folderName)
                car1.setInGameName(userPref['livery_name'])
                car1.setRaceNumber(userPref['race_number'])
                await interaction.response.defer()
                car1.createDazzle()
                car1.createJsonFile()
                await interaction.followup.send('finishing touches...')
                car1.zipCar()
                print(car1.getZipPath())
                await interaction.followup.send(
                    content=f"Here is your {car.name}, you should probably change the name of the .json file",
                    file=discord.File(car1.getZipPath()))
            else:
                await interaction.response.send_message(f"User not found try /carpreferences first", ephemeral=True)
        except sqlite3.Error as e:
            print("SQLite error:", e)
        finally:
            conn.close()  # Make sure to close the connection when done
    else:
        await interaction.response.send_message(f"You are not permitted to do that", ephemeral=True)


@bot.tree.command(name="myreviracing",
                  description='iRacing Revsport Livery based on preferences set in /carpreferences')
@discord.app_commands.describe(car="Car model in iRacing")
@discord.app_commands.choices(car=iracingChoices)
async def myCar(interaction: discord.Interaction, car: discord.app_commands.Choice[int]):
    if interaction.user.id not in blacklist:
        try:
            conn = sqlite3.connect("preferences.db")
            cur = conn.cursor()
            user_id = int(interaction.user.id)
            cur.execute("SELECT * FROM user WHERE id = ?", (user_id,))
            user_data = cur.fetchone()  # Assuming you're expecting one row
            if user_data:
                column_names = [description[0]
                                for description in cur.description]
                userPref = dict(zip(column_names, user_data))
                car1 = iRacingLivery()
                chosen = {}
                await interaction.response.defer()
                for x in iracingCars:
                    if x["value"] == car.value:
                        chosen = x
                        break
                daze1 = hexToTuple(userPref['dazzle1'])
                daze2 = hexToTuple(userPref['dazzle2'])
                base = hexToTuple(userPref['base_colour'])
                car1.set_car(chosen['file'])
                car1.set_dazzle1(daze1)
                car1.set_dazzle2(daze2)
                car1.set_base_colour(base)
                await interaction.followup.send('finishing touches...')
                specMap, carPath = car1.create_livery()
                await interaction.followup.send(
                    content=f"Here is your {chosen['key']}, upload it on trading paints under 'Just Me' ",
                    files=[discord.File(specMap), discord.File(carPath)])
            else:
                await interaction.response.send_message(f"User not found try /carpreferences first", ephemeral=True)
        except sqlite3.Error as e:
            print("SQLite error:", e)
        finally:
            conn.close()  # Make sure to close the connection when done
    else:
        await interaction.response.send_message(f"You are not permitted to do that", ephemeral=True)


@bot.tree.command(name="myreviracing2",
                  description='iRacing Revsport Livery based on preferences set in /carpreferences')
@discord.app_commands.describe(car="Car model in iRacing")
@discord.app_commands.choices(car=iracingChoices1)
async def myCar(interaction: discord.Interaction, car: discord.app_commands.Choice[int]):
    if interaction.user.id not in blacklist:
        try:
            conn = sqlite3.connect("preferences.db")
            cur = conn.cursor()
            user_id = int(interaction.user.id)
            cur.execute("SELECT * FROM user WHERE id = ?", (user_id,))
            user_data = cur.fetchone()  # Assuming you're expecting one row
            if user_data:
                column_names = [description[0]
                                for description in cur.description]
                userPref = dict(zip(column_names, user_data))
                car1 = iRacingLivery()
                chosen = {}
                await interaction.response.defer()
                for x in iracingCars1:
                    if x["value"] == car.value:
                        chosen = x
                        break
                daze1 = hexToTuple(userPref['dazzle1'])
                daze2 = hexToTuple(userPref['dazzle2'])
                base = hexToTuple(userPref['base_colour'])
                car1.set_car(chosen['file'])
                car1.set_dazzle1(daze1)
                car1.set_dazzle2(daze2)
                car1.set_base_colour(base)
                await interaction.followup.send('finishing touches...')
                specMap, carPath = car1.create_livery()
                await interaction.followup.send(
                    content=f"Here is your {chosen['key']}, upload it on trading paints under 'Just Me' ",
                    files=[discord.File(specMap), discord.File(carPath)])
            else:
                await interaction.response.send_message(f"User not found try /carpreferences first", ephemeral=True)
        except sqlite3.Error as e:
            print("SQLite error:", e)
        finally:
            conn.close()  # Make sure to close the connection when done
    else:
        await interaction.response.send_message(f"You are not permitted to do that", ephemeral=True)


bot.run(token)

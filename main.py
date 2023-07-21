import random
import discord
import os
import shutil
import datetime
from liveryClasses import accCarModels, ACCLivery
from discord.ext import commands


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


currentDirectory = os.getcwd()
tempDirectory = os.path.join(currentDirectory, 'temp')


def clearTempDirectory():
    shutil.rmtree(tempDirectory)
    os.mkdir("temp")


# This example requires the 'members' and 'message_content' privileged intents to function.

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='xm3',
                   description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def uptime(ctx):
    currentTime = datetime.datetime.now()
    difference = (currentTime - startTime).total_seconds() / 60
    await ctx.send(f'This bot has been running for {difference} minutes since {str(startTime)}')


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def die(ctx):
    await ctx.send('zamn')
    quit()


class carDropdown(discord.ui.Select):
    def __init__(self):
        options = []
        for car in cars:
            options.append(discord.SelectOption(
                label=car["key"], description='Select this for a '+car['key']+' livery.', emoji='🏎️'))

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose a car',
                         min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f'You selected the {self.values[0]}')
        for car in cars:
            if car['key'] == self.values[0]:
                newCarLivery.setCarModelType(car['value'])
                break


class carDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        dropdown = carDropdown()
        self.add_item(dropdown)
        baseMat = baseMatDropdown()
        self.add_item(baseMat)


class baseMatDropdown(discord.ui.Select):
    def __init__(self):
        options = []
        for mat in materials:
            options.append(discord.SelectOption(
                label=mat["key"], description='Select this for a '+mat['key']+' base.', emoji='🎨'))

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose a base material',
                         min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f'You selected a {self.values[0]} finish')
        for car in cars:
            if car['key'] == self.values[0]:
                newCarLivery.setBaseMaterialId(car['value'])
                break




@bot.command()
async def Car(ctx):
    carView = carDropdownView()
    # Sending a message containing our view
    await ctx.send('Pick the car for your new livery:', view=carView)

class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Red', description='Your favourite colour is red', emoji='🟥'),
            discord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            discord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦'),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f'Your favourite colour is {self.values[0]}')


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())
        self.add_item(Dropdown())


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')



@bot.command()
async def colour(ctx):
    """Sends a message with our dropdown containing colours"""

    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    await ctx.send('Pick your favourite colour:', view=view)


bot.run('MTEyOTE5MDk3MTc5NjYzNTY0OA.GRSyl9.HIHgEWFNQ-VTt1MiyRYZDF41iutxWUAussL-So')

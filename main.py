# To do: For the next version, abandon the workings with mysql and use a discord server itself to read and write the data.
# Also, I want the bot to (once it comes online) parse through its database to check wether it has left out a few entries.
# If it did, I want it to start it's count once again.
# So when the bot starts, one thing it needs to do is start a process of count (if required) and stop that process after the work is done.
# This should be done while the bot is online and waiting for any other commands...but I don't want the initial process to get stuck and keep going due to the
# new commands that are entered. So those two things should be two separate entities.
  
# ---------- importing the important libraries --------------- #
import discord
import asyncio
from os import getenv
from time import strftime
from dotenv import load_dotenv
from discord.ext import commands  # for using commands.Bot() instead of discord.Client()
from get_data import qdata, rdata, Delete
  # ------------------------------------------------------------ #

  # ------------------ connection and stuff -------------------- #
load_dotenv()  # For parsing the .env file
TOKEN = getenv('TOKEN')  # Get TOKEN
ID = int(getenv('ID'))
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='gg', intents=intents)  # connection to discord (through the command section module)
#  Note: class discord.ext.commands.Bot() is a subclass of discord.client

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}\n{bot.user.id}\n------")  # bot.user is the 'bot'
	await bot.change_presence(activity=discord.Game("gghelp"))  # will display as "playing !help"
  # ------------------------------------------------------------ #

bot.remove_command('help')

@bot.command()
async def help(ctx):
	embed = discord.Embed(colour = discord.Colour.green())
	embed.set_author(name = 'Help: \nShows this message')
	embed.add_field(name = 'info', value = 'Gives info on the bot', inline = False)
	embed.add_field(name = 'all', value = 'List of all available commands', inline = False)
	await ctx.send(embed = embed)


@bot.command()	
async def info(ctx):
	embed = discord.Embed(colour = discord.Colour.purple())
	embed.set_author(name = 'Info')
	embed.add_field(name = 'What is it?', value = 'A discord bot made using python for helping you keep track of your goals', inline = False)
	embed.add_field(name = 'Creator', value = 'Made by \'Hemant\'', inline = False)
	embed.add_field(name = 'Source code', value = 'https://github.com/r3a10god/The-goal-setting-bot', inline = False)
	await ctx.send(embed = embed)


@bot.command()
async def all(ctx):	
	embed = discord.Embed(colour = discord.Colour.red())
	embed.set_author(name = 'All commands of The-goal-setting-bot')
	embed.add_field(name = 'reg', value = '''Register your goal and the time period with this command.
    	Format:
    	ggreg <day(00) hour(00) month(00) sec(00)> <message>''', inline = False)
	embed.add_field(name = 'End', value = 'We\'ll be coming with new features soon', inline = False)
	await ctx.send(embed = embed)

  # --------------- the main commands -------------------------- #
@bot.command()  # getting user input to show in console
async def reg(ctx, d:str, h:str, m:str, s:str, *, content:str):
    T = int(strftime("%Y%m%d%H%M%S"))
    T = str(T + int(d + h + m + s))
    rdata(ctx.author.id, content, T)
    #asyncio.get_event_loop().run_until_complete(checkDate(ctx.author.id))
    await checkDate(ctx.author.id)


async def send(uid):
	'''This function sends the registered message to the user with user_id = uid'''
	query = qdata(uid)  # get data for user 
	user = bot.get_user(uid)
	await user.send(query)


async def checkDate(uid):
	'''This function will continuously check wether the deadline has been reached'''
	date = qdata(uid, query='date')  # this will return reminder date (timestamp) as int
	T = int(strftime("%Y%m%d%H%M%S"))  # this will return [current] date (timestamp) as int
	while T < date:
		#asyncio.sleep(5)  # this will update 'T' every 5 seconds
		T = int(strftime("%Y%m%d%H%M%S"))
	else:
		await send(uid)  # if either the deadline has reached or has been passed then send(uid)
		Delete(uid)  # delete the reminder from the database
  # ------------------------------------------------------------ #

bot.run(TOKEN)

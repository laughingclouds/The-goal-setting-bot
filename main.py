  # ---------- importing the important libraries --------------- #
import discord
import asyncio
from os import getenv
from get_data import *
from time import strftime
from dotenv import load_dotenv
from discord.ext import commands  # for using commands.Bot() instead of discord.Client()
  # ------------------------------------------------------------ #

  # ------------------ connection and stuff -------------------- #
load_dotenv()  # For parsing the .env file
TOKEN = getenv('TOKEN')  # Get TOKEN
ID = int(getenv('ID'))
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)  # connection to discord (through the command section module)
#  Note: class discord.ext.commands.Bot() is a subclass of discord.client

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}\n{bot.user.id}\n------")  # bot.user is the 'bot'
	await bot.change_presence(activity=discord.Game("!help"))  # will display as "playing !help"
  # ------------------------------------------------------------ #

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

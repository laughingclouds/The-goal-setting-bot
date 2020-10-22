import discord
from os import getenv
from random import randint
from get_data import regdata
from dotenv import load_dotenv
from discord.ext import commands  # for using commands.BOT() instead of discord.Client()


load_dotenv()  # For parsing the .env file
TOKEN = getenv('TOKEN')  # Get TOKEN
ID = int(getenv('ID'))
bot = commands.Bot(command_prefix='!')  # connection to discord (through the command section module)
#  Note class discord.ext.commands.Bot() is a subclass of discord.client

@bot.event
async def on_ready():
	print(f'Log in successful as {bot.user}')  # bot.user is the "bot"
	bot.change_presence(activity=discord.Game("!help"))  # will display as "playing !help"


@bot.command()  # command information--do later
async def info(ctx):
	embed_var = discord.Embed(title="Test", color=0x6c0101)
	embed_var.add_field(name="First", value="This is a test", inline=False)
	embed_var.add_field(name="Second", value="This is another test", inline=False)
	await ctx.send(embed=embed_var)
	
@bot.command()	# getting user input to show in console
async def register(ctx, *, content:str):
	regdata(ctx.author, content)
	
	
bot.run(TOKEN)

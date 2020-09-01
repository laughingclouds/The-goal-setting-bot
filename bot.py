import discord
from os import getenv
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


@bot.command()  # command information--do later
async def info(ctx):
	embed_var = discord.Embed(title="Test", color=0x6c0101)
	embed_var.add_field(name="First", value="This is a test", inline=False)
	embed_var.add_field(name="Second", value="This is another test", inline=False)
	await ctx.send(embed=embed_var)

#  'ctx' has all the information about the message/command you send
@bot.command()
async def ping(ctx):
	'''
	This command is to check the latency of the bot.
	btw, 'await' is to stop the async flow of the funct to make it do what I want it to do in the meantime.
	'''
	await ctx.send(f"{ctx.message.author.mention}, here's the latency: {bot.latency}")


@bot.command()
async def echo(ctx, *, content:str):  # '*' represents all arguements belonging to 'content' as a str
	await ctx.send(f"\"{content}\"")


@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.startswith("&hello"):
		await message.channel.send(f"{message.author.mention} hi!")
	await bot.process_commands(message)


@bot.command()
async def users(ctx):
	guild = bot.get_guild(ID)
	await ctx.send(f"\'{guild.name}\' has {guild.member_count} members (including bots)")


bot.run(TOKEN)

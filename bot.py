import discord
from os import getenv
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()  # For parsing the .env file
TOKEN  = getenv('TOKEN')  # Get TOKEN
client = commands.Bot(command_prefix='!')  # connection to discord (through the command section module)
#  Note class discord.ext.commands.Bot() is a subclass of discord.client

@client.event
async def on_ready():
	print(f'Log in successful as {client.user}')  # print message on console


@client.command()
async def info(ctx):
	embed_var = discord.Embed(title="Test", color=0x6c0101)
	embed_var.add_field(name="First", value="This is a test", inline=False)
	embed_var.add_field(name="Second", value="This is another test", inline=False)
	await ctx.send(embed=embed_var)


@client.command()
async def ping(ctx):
	await ctx.send("pong!")

client.run(TOKEN)

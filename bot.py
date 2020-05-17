import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Set Enviroment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
	print(f'Logged in as: {bot.user.name}')
	print(f'With ID: {bot.user.id}')


@bot.command()
async def ping(ctx):
	await ctx.send('pong')


bot.run(TOKEN)
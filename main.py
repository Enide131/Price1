import discord
import json
from discord.ext import commands

file = open('config.json', 'r')
config = json.load(file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='clendoska')

async def ping(ctx):
    await ctx.send(f'{ctx.author.mention}4 polosy')

@bot.command(name='natochenykinjal')

async def ping(ctx):
    await ctx.send(f'{ctx.author.mention}20 polos')

bot.run(config['token'])
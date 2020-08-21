import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!\n')
    print(bot.guilds)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)

@bot.command(name='test')
async def test(ctx, *args):
    await ctx.send('Your message was: ' + ' '.join(args))

bot.run(TOKEN)

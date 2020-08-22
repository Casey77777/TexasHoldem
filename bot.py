import os

import discord
from dotenv import load_dotenv


from table import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='.')

table = Table()

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

@bot.command()
async def commands(ctx, *args):
    message = ''
    for command in bot.commands:
        message += f'{command}\n'
    await ctx.send(message)

@bot.command()
async def join(ctx, *args):
    global table
    author = ctx.message.author

    try:
        table.add_player(author)
    except ValueError:
        await ctx.send(f'{author.name} is already at the table.')
        return

    await ctx.send(f'{author.name} joined the table!')

@bot.command()
async def leave(ctx, *args):
    global table
    author = ctx.message.author

    try:
        table.remove_player(author)
    except ValueError:
        await ctx.send(f'{author.name} is already away from the table.')
        return

    await ctx.send(f'{author.name} left the table.')

@bot.command()
async def reset_table(ctx, *args):
    global table
    table = Table()
    await ctx.send('Table has reset!')

@bot.command()
async def players(ctx, *args):
    global table
    player_names = []
    for player in table.players:
        player_names.append(player.name)
    if len(player_names) == 0:
        await ctx.send('Players: [none]')
        return
    await ctx.send('Players: { ' + ', '.join(player_names) + ' }')

# @bot.command(name='test')
# async def test(ctx, *args):
#     await ctx.send('Your message was: ' + ' '.join(args))

bot.run(TOKEN)

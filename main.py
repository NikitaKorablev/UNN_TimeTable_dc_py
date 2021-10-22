import os

from discord.ext import commands
from dotenv import load_dotenv
from timetable import read_only, main_loop, write_only

load_dotenv()
TOKEN_DS = os.getenv('DISCORD_TOKEN')

channels = [int(os.getenv(f'CHN{i}')) for i in range(1,6)]

bot = commands.Bot(command_prefix='!')
MODE = 2


@bot.event
async def on_ready():
    await main_loop(bot, channels, MODE)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.command(name='log_print', help='printing log.txt')
@commands.has_role('Administrator')
async def log_print(ctx):
    message = await read_only()
    await ctx.send(message)


@bot.command(name='log_set', help='rewriting log.txt')
@commands.has_role('Administrator')
async def log_set(ctx, *arg):
    await write_only(f'{arg[0]} {arg[1]}\n{arg[2]} {arg[3]}')
    await ctx.send('New Log is ready')
    await main_loop(bot, channels, MODE)


@bot.command(name='mode_set', help='changing work mode')
@commands.has_role('Administrator')
async def mode_set(ctx, arg):
    global MODE
    MODE = int(arg)
    await ctx.send(f'Switch mode to {MODE}')


@bot.command(name='mode_print', help=f'0 - Расп-,Чист-,Vk-,Log-'
                                     f'1 - Расп+,Чист+,Vk-,Log-'
                                     f'2 - Расп+,Чист+,Vk+,Log+')
@commands.has_role('Administrator')
async def mode_print(ctx):
    global MODE
    await ctx.send(f'Now mode is {MODE}')


bot.run(TOKEN_DS)

import discord
import os
import asyncio
from discord.ext import commands
from timetable import timetable as tt
from timetable import table_chat as tc
import datetime
import schedule
import time
from multiprocessing import Process, freeze_support
from timetable import time_client


'''https://github.com/Rapptz/discord.py/blob/v1.7.3/examples/basic_voice.py'''

token = 'ODY4OTE0ODM3MTY0NTIzNjAw.YP2mAA.U9gat4BT3GYfH0NQrxZIJwHutI0'
client = commands.Bot(command_prefix='!')

# def client__command(client):
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cog.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cog.{extension}')

for filename in os.listdir('./cog'):
    if filename.endswith('.py'):
        client.load_extension(f'cog.{filename[:-3]}')


# def time():
#     date, time = str(datetime.datetime.now()).split()
#
#     date = date.split('-')
#     date = date[2]+'.'+date[1]+'.'+date[0]
#     time



# time_client(client)

if __name__ == '__main__':
    freeze_support()
    p2 = Process(target=time_client(client))
    p2.start()



client.run(token)

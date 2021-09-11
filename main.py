import discord
from discord.ext import commands
from timetable import time_client
import os

'''https://github.com/Rapptz/discord.py/blob/v1.7.3/examples/basic_voice.py'''

token = 'ODg1MjYzMDgxOTI2NzA1Mjcy.YTkffg.xgOESEJsLqpTMqVGPxoRWdDUKx4'
client = commands.Bot(command_prefix='!')

data_1 = []
data_2 = []
data_3 = []
data_4 = []
data_5 = []


# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cog.{extension}')
#
#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cog.{extension}')
#
#
# for filename in os.listdir('./cog'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cog.{filename[:-3]}')

# channels = [868936978157162516]
channels = [882231588832804877, 884135605150289920, 884135626855837757, 884135649614106685, 884135682371637278]

time_client(client, channels)


# @client.event
# async def on_message(ctx, message):
#     author = '{0.author}'.format(message)
#     print(author)

client.run(token)

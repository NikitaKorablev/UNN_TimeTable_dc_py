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

token = 'ODg1MjYzMDgxOTI2NzA1Mjcy.YTkffg.xgOESEJsLqpTMqVGPxoRWdDUKx4'
client = commands.Bot(command_prefix='!')


# def time():
#     date, time = str(datetime.datetime.now()).split()
#
#     date = date.split('-')
#     date = date[2]+'.'+date[1]+'.'+date[0]
#     time


time_client(client)


client.run(token)

from discord.ext import commands
from timetable import time_client


'''https://github.com/Rapptz/discord.py/blob/v1.7.3/examples/basic_voice.py'''

token = 'ODg1MjYzMDgxOTI2NzA1Mjcy.YTkffg.xgOESEJsLqpTMqVGPxoRWdDUKx4'
client = commands.Bot(command_prefix='!')

time_client(client)

client.run(token)

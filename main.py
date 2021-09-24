from discord.ext import commands
from timetable import time_client

token = 'ODg1MjYzMDgxOTI2NzA1Mjcy.YTkffg.xgOESEJsLqpTMqVGPxoRWdDUKx4'
client = commands.Bot(command_prefix='!')

channels = [868936978157162516]
# channels = [882231588832804877, 884135605150289920, 884135626855837757, 884135649614106685, 884135682371637278]

time_client(client, channels)

client.run(token)

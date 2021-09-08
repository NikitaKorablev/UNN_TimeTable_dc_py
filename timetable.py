import discord
from discord.ext import commands

import datetime
import requests
import time

groups = ['34883', '34884', '34885', '36374', '36436']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36'}


def timetable(group, date):
    st, fin = st_fin(date)
    url = 'https://portal.unn.ru/ruzapi/schedule/group/' + groups[group]
    response = requests.get(url, headers=HEADERS, params={
        'start': st,  # 'start': '2021.09.06',
        'finish': fin,  # 'finish': '2021.09.12',
        'lng': 1
    }).json()
    table_need = [
        {j: i[j] for j in i.keys()}
        for i in response if i['date'] == date.replace('-', '.')]

    return table_need


def print_table(table, date):
    print('Расписание на', date)
    for i in table:
        print(f"""------------------------------------------------------------------------------------------------------—
{i['discipline']}
------------------------------------------------------------------------------------------------------—
{i['beginLesson']} - {i['endLesson']}
{i['lecturer']} | {i['kindOfWork']}""")
        if i['building'] == 'Виртуальное':
            print('Ссылка:' + '\n')
        else:
            print(i['auditorium'], i['building'] + '\n')


def table_chat(table, date):
    date = '.'.join(date.split('-')[::-1])
    chat = 'Расписание на ' + date + '\n'
    chat_array = [chat]
    for i in table:
        group = i['group'] if i['group'] else i['stream']
        a = '-' * 100 + '\n'
        chat = a + i['discipline'] + ' | ' + group + '\n' + a + i['beginLesson'] + ' - ' + i['endLesson'] + \
                '\n' + i['lecturer'] + ' | ' + i['kindOfWork'] + '\n'

        if i['building'] == 'Виртуальное':
            chat += 'Ссылка:' + '\n'
        else:
            chat += i['auditorium'] + ' ' + i['building'] + '\n'

        chat_array.append(chat)

    return chat_array


def st_fin(date):
    date_s = list(map(int, date.split('-')))
    today = datetime.date(*date_s)
    for i in range(7):
        a = today + datetime.timedelta(days=-i)
        if datetime.datetime.isoweekday(a) == 1:
            break
    b = a + datetime.timedelta(days=6)
    st = str(a).replace('-', '.')
    fin = str(b).replace('-', '.')
    return [st, fin]


if __name__ == '__main__':
    print(datetime.date.today())
    print(datetime.datetime.now())
    DATE = '12.09.2021'
    GROUP = 1

    table = timetable(GROUP, DATE)  # список словарей пар
    print_table(table, DATE)


def time_posting(std_time):
    hour, minutes = map(int, std_time.split(':'))

    now_d = datetime.datetime.now()
    next_day = now_d + datetime.timedelta(days=1)
    # hours_next_day, minutes_next_day, _ = list(map(int, str(next_day).split()[1].split(':')))
    next_day = list(map(int, str(next_day).split()[0].split('-')))
    next_day = datetime.datetime(*next_day, hour, minutes, 0)

    h, m, sec = [int(float(i)) for i in str(next_day - now_d).split(':')]

    time_before_next_posting = int(sec + m*60 + h*3600)

    return time_before_next_posting


def time_client(client):
    @client.event
    async def on_ready():
        while True:
            channels = [868936978157162516]
            # channels = [882231588832804877, 884135605150289920, 884135626855837757, 884135649614106685,
            #             884135682371637278]
            DATE, TIME = str(datetime.datetime.now() + datetime.timedelta(days=1)).split()
            for i, j in enumerate(channels):
                GROUP = i
                CHANNEL = j
                table = timetable(GROUP, DATE)
                channel = client.get_channel(CHANNEL)

                for message in table_chat(table, DATE):
                    await channel.send(message)

            tp = time_posting(std_time='20:0')

            time.sleep(tp)




    #     for guild in self.client.guilds:
    #         for channel in guild.text_channels:
    #             self.text_channel_list.append(channel)
    #             print(self.text_channel_list)

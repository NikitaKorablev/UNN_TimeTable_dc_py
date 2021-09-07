import discord
from discord.ext import commands

import requests
import datetime
import time

groups = ['34883', '34884', '34885', '36374', '36436']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36'}
session = requests.session()
session.headers.update(headers)
auth = ('', '') #логин, пароль
login = session.get('https://portal.unn.ru/stream/', auth=auth)

needs = ['auditorium', 'beginLesson', 'endLesson', 'building', 'date', 'dayOfWeek', 'dayOfWeekString', 'discipline',
         'kindOfWork', 'lecturer']


def timetable(group, date):
    date = date.split('.')
    date = date[2] + '.' + date[1] + '.' + date[0]
    st, fin = st_fin(date)
    url = 'https://portal.unn.ru/ruzapi/schedule/group/' + groups[group - 1]
    response = session.get(url, params={
        'start': st,  # 'start': '2021.09.06',
        'finish': fin,  # 'finish': '2021.09.12',
        'lng': 1
    }).json()
    table_need = [
        {j: i[j] for j in needs}
        for i in response if i['date'] == date]

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
    chat = 'Расписание на ' + date + '\n'
    for i in table:
        a = '-'*100 + '\n'
        chat += a + i['discipline'] + '\n' + a + i['beginLesson'] + ' - ' + i['endLesson'] +\
                '\n' + i['lecturer'] + ' | ' + i['kindOfWork'] + '\n'

        if i['building'] == 'Виртуальное':
            chat += 'Ссылка:' + '\n'
        else:
            chat += i['auditorium'] + ' ' + i['building'] + '\n'

    return chat


def st_fin(date):
    date_s = date.split('.')
    for i in range(len(date_s)):
        date_s[i] = int(date_s[i]) if date_s[i][0] != '0' else int(date_s[i][-1])
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

    table = timetable(GROUP, DATE) #список словарей пар
    print_table(table)


def time_client(client):

    @client.event
    async def on_ready():
        while True:
            channels = ['868936978157162516']
            print(channels)

            DATE = '10.09.2021'
            GROUP = 1
            table = timetable(GROUP, DATE)

            for text_channel in channels:
                channel = client.get_channel(int(text_channel))
                await channel.send(table_chat(table, DATE))

            time.sleep(30)



    #     for guild in self.client.guilds:
    #         for channel in guild.text_channels:
    #             self.text_channel_list.append(channel)
    #             print(self.text_channel_list)




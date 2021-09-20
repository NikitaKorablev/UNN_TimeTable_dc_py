import datetime
import requests
import time
from web import web

groups = ['3821Б1ФИ1', '3821Б1ФИ2', '3821Б1ФИ3', '3821Б1ФИ4', '3821Б1ФИ5']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36'}


def timetable(group, date):
    url = 'https://portal.unn.ru/ruzapi/schedule/group/' + group_id(group)
    response = requests.get(url, headers=HEADERS,  params={
        'start': date.replace('-', '.'),  # 'start': '2021.09.06',
        'finish': date.replace('-', '.'),  # 'finish': '2021.09.12',
        'lng': 1
    }).json()
    # print(response)
    # print('response: ', response.url)
    return response


def group_id(group):
    url = 'https://portal.unn.ru/ruzapi/search'
    response = requests.get(url, headers=HEADERS, params={
        'type': 'group',
        'term': group.encode()
    })
    id = response.json()[0]['id']
    return id


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
    dow_str = table[0]['dayOfWeekString']

    date = '.'.join(date.split('-')[::-1])
    chat = 'Расписание на ' + date + '\n'
    chat_array = [chat]
    for i in table:
        group = i['group'] if i['group'] else i['stream']
        a = '-' * 59 + '\n'
        lesson = i['discipline']
        kindOfWork = i['kindOfWork']
        beginLesson = i['beginLesson']

        chat = '\n' + a + lesson + ' | ' + group + '\n' + a + beginLesson + ' - ' + i['endLesson'] + '\n'

        if i['building'] == 'Виртуальное':
            chat += i['lecturer'] + '\n'
            chat += web(dow_str, lesson, kindOfWork, beginLesson)
            # print(2)
        else:
            chat += i['auditorium'] + ' ' + i['building'] + '\n'
            chat += i['lecturer'] + ' | ' + kindOfWork

        print(chat)

        chat_array.append(chat)
    return chat_array


def time_posting(std_time, ddd):
    hour, minutes = map(int, std_time.split(':'))

    now_d = datetime.datetime.now()
    next_day = now_d + datetime.timedelta(days=ddd)
    # hours_next_day, minutes_next_day, _ = list(map(int, str(next_day).split()[1].split(':')))
    next_day = list(map(int, str(next_day).split()[0].split('-')))
    next_day = datetime.datetime(*next_day, hour, minutes, 0)

    if ',' in str(next_day - now_d):
        day, clock = str(next_day - now_d).split(',')
        h, m, sec = [int(float(i)) for i in clock.split(':')]
        day = int(day.split()[0])
    else:
        h, m, sec = [int(float(i)) for i in str(next_day - now_d).split(':')]
        day = 0

    time_before_next_posting = int(sec + m*60 + h*3600 + day*24*3600)

    # print("days:", day, ";", "hours:", h, ";", "minutes:", m, ";", "seconds: ", sec)
    # print(time_before_next_posting, 'second')

    return time_before_next_posting


def time_client(client, channels):
    @client.event
    async def on_ready():
        isFirstTry = True
        while True:
            if not(isFirstTry):
                tp = time_posting(std_time='20:00', ddd=1)
                time.sleep(tp)

            isFirstTry = False
            DATE, TIME = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1, hours=3)).split()
            for i, j in enumerate(channels):
                GROUP = groups[i]
                CHANNEL = j
                table = timetable(GROUP, DATE)
                channel = client.get_channel(CHANNEL)

                if table:
                    for message in table_chat(table, DATE):
                    #     await channel.send(message)
                        pass

            # time.sleep(60)

            # print(tp)




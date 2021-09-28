import datetime
import requests
import time
from web import web

token_vk = 'c1b9bdf4ff6b9ad047e305bc0cbf0986a922e7679fdc6bb9f60cb6cbb6c52a0d29635a9afb9b9f230d6e2'
id_vk = 206866428
groups = ['3821Б1ФИ1', '3821Б1ФИ2', '3821Б1ФИ3', '3821Б1ФИ4', '3821Б1ФИ5']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36'}


def send_message(id, message, token):
    resp = requests.post('https://api.vk.com/method/messages.send', params={
        'user_id': id,
        'random_id': int(time.time())-100000,
        'access_token': token,
        'v': 5.131,
        'message': message
    })
    return resp.status_code


def timetable(group, date):
    url = 'https://portal.unn.ru/ruzapi/schedule/group/' + group_id(group)
    response = requests.get(url, headers=HEADERS, params={
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

        # print(chat)

        chat_array.append(chat)
    return chat_array


def time_posting(std_time):
    test_arr = []
    hour, minutes = map(int, std_time.split(':'))

    now_d = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
    now_d = str(now_d).split('.')[0].split()
    now_d_date = list(map(int, now_d[0].split('-')))
    now_d_time = list(map(int, now_d[1].split(':')))
    now_d = datetime.datetime(now_d_date[0], now_d_date[1], now_d_date[2], now_d_time[0], now_d_time[1], now_d_time[2])

    next_day = now_d + datetime.timedelta(days=1)
    next_day = list(map(int, str(next_day).split()[0].split('-')))
    next_day = datetime.datetime(*next_day, hour, minutes, 0)

    if ',' in str(next_day - now_d):
        day, clock = str(next_day - now_d).split(',')
        h, m, sec = [int(float(i)) for i in clock.split(':')]
        day = int(day.split()[0])
    else:
        h, m, sec = [int(float(i)) for i in str(next_day - now_d).split(':')]
        day = 0

    time_before_next_posting = int(sec + m * 60 + h * 3600 + day * 24 * 3600)

    # print("days:", day, ";", "hours:", h, ";", "minutes:", m, ";", "seconds: ", sec)
    # send_message(id_vk, f'Time posting: days: {day}; hours: {h}; minutes: {m}; seconds: {sec}', token_vk)

    return time_before_next_posting


def time_client(client, channels):
    @client.event
    async def on_ready():
        isFirstTry = True
        while True:
            if not (isFirstTry):
                tp = time_posting(std_time='20:00')
                time.sleep(tp)

            isFirstTry = False

            DATE, TIME = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1, hours=3)).split()

            # print(str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)))  # Распечатать
            # send_message(id_vk, 'Time now (+3): ' + str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)), token_vk)

            for i, j in enumerate(channels):
                GROUP = groups[i]
                CHANNEL = j
                table = timetable(GROUP, DATE)
                channel = client.get_channel(CHANNEL)

                # await channel.send("time: " + str(datetime.datetime.now()))

                if table:
                    for message in table_chat(table, DATE):
                        # await channel.send(message)
                        pass


import datetime
import requests
import time

groups = ['3821Б1ФИ1', '3821Б1ФИ2', '3821Б1ФИ3', '3821Б1ФИ4', '3821Б1ФИ5']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36'}


def timetable(group,date):
    url = 'https://portal.unn.ru/ruzapi/schedule/group/' + group_id(group)
    response = requests.get(url,headers=HEADERS,  params={
        'start': date.replace('-', '.'),  # 'start': '2021.09.06',
        'finish': date.replace('-', '.'),  # 'finish': '2021.09.12',
        'lng': 1
    }).json()
    print(type(response[0]['dayOfWeek']))
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
    date = '.'.join(date.split('-')[::-1])
    chat = 'Расписание на ' + date + '\n'
    chat_array = [chat]
    for j, i in enumerate(table):
        group = i['group'] if i['group'] else i['stream']
        a = '-' * 59 + '\n'
        lesson = i['discipline']

        chat = a + lesson + ' | ' + group + '\n' + a + i['beginLesson'] + ' - ' + i['endLesson'] + '\n'

        if i['building'] == 'Виртуальное':
            chat += 'Ссылка: ' + str(j + 1) + '\n'
        else:
            chat += i['auditorium'] + ' ' + i['building'] + '\n'

        chat += i['lecturer'] + ' | ' + i['kindOfWork'] + '\n'

        chat_array.append(chat)

    return chat_array


def time_posting(std_time):
    hour, minutes = map(int, std_time.split(':'))

    now_d = datetime.datetime.now()
    next_day = now_d + datetime.timedelta(days=1)
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

    print("days:", day, ";", "hours:", h, ";", "minutes:", m, ";", "seconds: ", sec)
    print(time_before_next_posting, 'second')

    return time_before_next_posting


def time_client(client, channels):
    math_analysis_monday = ['https://zoom.us/j/92825618536?pwd=NkUrbWxiTmlNQkRKVjQ', '928 2561 8536', '559912']
    math_analysis_thursday = ['https://zoom.us/j/98478027286?pwd=ZDRnZ1lvOWt0TDhGMGY', '984 7802 7286', '504739']
    math_analysis = [math_analysis_monday, math_analysis_thursday]

    base_programming = ['https://teams.microsoft.com/l/meetup-j...QwNWE1O',
                        'https://teams.microsoft.com/l/meetup-j...RiMmNjM']
    # base_programming[0] = 09:10
    # base_programming[1] = 14:40

    year, month, day = map(int, str(datetime.datetime.now()).split()[0].split('-'))
    week_day = datetime.date(year + 1, month, day).weekday()
    print(week_day)
    
    @client.event
    async def on_ready():
        while True:
            DATE, TIME = str(datetime.datetime.now() + datetime.timedelta(days=1)).split()
            for i, j in enumerate(channels):
                GROUP = groups[i]
                CHANNEL = j
                table = timetable(GROUP, DATE)
                channel = client.get_channel(CHANNEL)

                # for message in table_chat(table, DATE):
                #     await channel.send(message)

            tp = time_posting(std_time='20:0')

            time.sleep(tp)

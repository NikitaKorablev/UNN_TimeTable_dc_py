import datetime
import requests
import time
from web import web

token_vk = 'c1b9bdf4ff6b9ad047e305bc0cbf0986a922e7679fdc6bb9f60cb6cbb6c52a0d29635a9afb9b9f230d6e2'
id_vk = 206866428
groups = ['3821Б1ФИ1', '3821Б1ФИ2', '3821Б1ФИ3', '3821Б1ФИ4', '3821Б1ФИ5']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36'}


def send_message(message, id_v=id_vk, token=token_vk):
    resp = requests.post('https://api.vk.com/method/messages.send', params={
        'user_id': id_v,
        'random_id': int(time.time()) - 100000,
        'access_token': token,
        'v': 5.131,
        'message': message + '\n' + read_only()
    })
    return resp.status_code


def timetable(group, date):
    url = 'https://portal.unn.ru/ruzapi/schedule/group/' + group_id(group)
    response = requests.get(url, headers=HEADERS, params={
        'start': date.replace('-', '.'),
        'finish': date.replace('-', '.'),
        'lng': 1
    }).json()
    return response


def group_id(group):
    url = 'https://portal.unn.ru/ruzapi/search'
    response = requests.get(url, headers=HEADERS, params={
        'type': 'group',
        'term': group.encode()
    })
    id_g = response.json()[0]['id']
    return id_g


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
        if not group: group = i['stream'] if i['stream'] else i['subGroup']
        a = '\n'+'-' * 59 + '\n'
        lesson = i['discipline']
        kindOfWork = i['kindOfWork']
        beginLesson = i['beginLesson']

        chat = f"{a}{lesson} | {group}{a} {beginLesson} - {i['endLesson']}\n{i['lecturer']}\n"

        chat += web(dow_str, lesson, kindOfWork, beginLesson)

        chat_array.append(chat)
    return chat_array

def read_only():
    with open("log.txt", "r") as f:
        return f.read()


def get_post_info(today, next_d, ask_day):
    with open("log.txt", "r") as f:
        post1, post2 = f.read().split('\n')
        p1_b, p1_d = post1.split()
        p2_b, p2_d = post2.split()

    if ask_day == 'today':
        if p1_d == today:
            return int(p1_b)
        if p2_d == today:
            return int(p2_b)
        return 0
    else:
        if p1_d == next_d:
            return int(p2_b)
        if p2_d == next_d:
            return int(p2_b)
        return 0


def set_post_info(today, next_d, ask_day):
    with open("log.txt", "r") as f:
        post1, post2 = f.read().split('\n')
        p1_b, p1_d = post1.split()
        p2_b, p2_d = post2.split()
    with open("log.txt", "w") as f:
        if ask_day == 'today':
            if p2_d == today:
                f.write(f'1 {today}\n')
                f.write(f'1 {today}')
            else:
                f.write(f'1 {today}\n')
                f.write(f'{post2}')
        else:
            if p2_d == today:
                f.write(f'{post2}\n')
                f.write(f'1 {next_d}')
            else:
                f.write(f'{post1}\n')
                f.write(f'1 {next_d}')


def time_posting(std, time_n, ask_day):
    t_n = list(map(int, time_n.split('.')[0].split(':')))
    for i in range(2):
        t_n[i] = t_n[i] * pow(60, 2-i)
        std[i] = std[i] * pow(60, 2-i)
    time_to_post = sum(std)-sum(t_n)
    if ask_day == 'today':
        return time_to_post
    else:
        return 24*pow(60,2)+time_to_post

HOUR = 19


def time_client(client, channels):
    @client.event
    async def on_ready():

        send_message("Reboot")
        while True:

            date_now, time_now = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)).split()
            date_next_d = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1, hours=3)).split()[0]

            ask_day = 'next day' if int(time_now.split(':')[0]) >= HOUR else 'today'
            ask_date = date_next_d if int(time_now.split(':')[0]) >= HOUR else date_now

            if not get_post_info(date_now, date_next_d, ask_day):
                for i, j in enumerate(channels):
                    table = timetable(groups[i], ask_date)
                    channel = client.get_channel(j)
                    await channel.purge()
                    if table:
                        for message in table_chat(table, ask_date):
                            await channel.send(message)
                            # pass
                set_post_info(date_now, date_next_d, ask_day)
                print(f'Расписание на {ask_day} отправлено')
                send_message(f'Расписание на {ask_day} отправлено')

            tp = time_posting([HOUR, 0, 0], time_now, ask_day)
            print(f'I sleep {tp} sec')
            send_message(f'I sleep {tp} sec')
            time.sleep(tp)

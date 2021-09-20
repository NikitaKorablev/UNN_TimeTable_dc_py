import datetime
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36'}


def timetable(group, date):
    url = 'https://portal.unn.ru/ruzapi/schedule/group/' + group_id(group)
    response = requests.get(url, headers=HEADERS, params={
        'start': date.replace('-', '.'),  # 'start': '2021.09.06',
        'finish': date.replace('-', '.'),  # 'finish': '2021.09.12',
        'lng': 1
    }).json()
    print()
    return response


def group_id(group):
    url = 'https://portal.unn.ru/ruzapi/search'
    response = requests.get(url, headers=HEADERS, params={
        'type': 'group',
        'term': group.encode()
    })
    id = response.json()[0]['id']
    return id


channels = [868936978157162516]
groups = ['3821Б1ФИ1']
for n in range(0, 6):
    DATE, TIME = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=n, hours=3)).split()
    for i, j in enumerate(channels):
        GROUP = groups[i]
        CHANNEL = j
        table = timetable(GROUP, DATE)
        # print(table)
        for k in range(len(table)):
            print(table[k]['kindOfWork'])



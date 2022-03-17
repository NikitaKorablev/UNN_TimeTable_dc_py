from time import time
from pytube import Playlist

def randRR():
    link = Playlist('https://www.youtube.com/playlist?list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p')
    n = int(time())%(link.length)
    return link.video_urls[n]

webs_lecture = { 
    'Вт': {
        'Математический анализ': {'link': 'https://zoom.us/j/99826311193?pwd=Q3p5SVZscTZZeHJaOFdMUk0xblBqQT09',
                                  'id': '998 2631 1193', 'pass': '334019'},
        'Дискретная математика': {'link': 'https://zoom.us/j/93532811483?pwd=WFZySm1BRjlHWExEeWxPR200SGpsZz09',
                                  'id': '935 3281 1483', 'pass': '123456'}
        # 'Теория информации': {'link': '', 'id': '', 'pass': ''}                 
    },

    'Пт': {
        'Основы программирования': {
            '07:30': {'link': 'https://teams.microsoft.com/l/meetup-join/19:meeting_M2I3Njg0MGItZTM2OS00ZDZlLWFjNWEtNTc1YzEzMjc2M2Nl@thread.v2/0?context={"Tid%22:%2260b6ee4f-43c2-4c1f-b509-d6fad245297a","Oid%22:%22e97f12bb-f589-4e7f-b5e2-92f59812fe83"}',
             'id': '', 'pass': ''},
            '10:50': {'link': 'https://teams.microsoft.com/l/meetup-join/19:meeting_NTlkOTc3MzEtMTUyMi00MWQ5LTg4MzgtZTJhNDAxODlkZTA2@thread.v2/0?context={"Tid%22:%2260b6ee4f-43c2-4c1f-b509-d6fad245297a","Oid%22:%22e97f12bb-f589-4e7f-b5e2-92f59812fe83"}',
             'id': '', 'pass': ''},
            '14:40': {'link': 'https://teams.microsoft.com/l/meetup-join/19:meeting_MTkzYTY3ZTMtNGUyNS00ODQ0LTgzODgtYmZjNDlmYzI0MGQw@thread.v2/0?context={"Tid%22:%2260b6ee4f-43c2-4c1f-b509-d6fad245297a","Oid%22:%22e97f12bb-f589-4e7f-b5e2-92f59812fe83"}',
             'id': '', 'pass': ''}
            # '10:50': {'link': randRR(), 'id': '', 'pass': ''}
        },
        'Алгебра и геометрия': {'link': 'https://zoom.us/j/6592432792?pwd=ZzIrWTM3NW11R1lIUzJ1YjRuUVVhdz09',
                                'id': '', 'pass': ''},
        'История (история России, всеобщая история)': {'link': 'https://zoom.us/j/9533347559?pwd=dVk2dUY4ejU0NVphQ1J5Mm1KOTIwUT09', 
                                'id': '953 334 7559', 'pass': '379248'}
    }
}
webs_practice = {
    'Вт': {
        '3821Б1ФИ1': {
            'Алгебра и геометрия': {'link': 'https://us04web.zoom.us/j/2685906294?pwd=WGFwZ0h4T2drZ3dhRkRKc00wZjNFZz09',
                                    'id': '268 590 6294', 'pass': 'gy2Ugd'},
            'Дискретная математика': {
                'link': 'https://us02web.zoom.us/j/84425798878?pwd=aEZ6UHFycEMrQjhtMlVQa2VHNWg4QT09',
                'id': '844 2579 8878', 'pass': '368668'}
        },
        '3821Б1ФИ2': {
            'Основы программирования': {
                '07:30': {'link': '', 'id': '', 'pass': ''},
                '09:10': {'link': '', 'id': '', 'pass': ''}}
        },
        '3821Б1ФИ3': {

        },
        '3821Б1ФИ4': {
            'Дискретная математика': {'link': '', 'id': '', 'pass': ''},
            'Основы программирования': {
                '09:10': {'link': '', 'id': '', 'pass': ''},
                '10:50': {'link': '', 'id': '', 'pass': ''}}
        },
        '3821Б1ФИ5': {
            'Алгебра и геометрия': {'link': '', 'id': '', 'pass': ''},
            'Практикум по математическому анализу': {'link': '', 'id': '', 'pass': ''}
        }
    },
    'Ср': {
        '3821Б1ФИ1': {
            'Практикум по математическому анализу': {
                'link': 'https://us04web.zoom.us/j/76741847077?pwd=MjNMQkllU1Q0eUR6Mm9WQ3NxVGJ6Zz09',
                'id': '767 4184 7077', 'pass': 'MMce1u'},
            'Основы программирования': {
                '09:10': {
                    'link': 'https://teams.microsoft.com/l/meetup-join/19:rWPbV6_vOw8UfOuxKfASaeFON_GjUhrmA3wzA9i22y81@thread.tacv2/1635251201883?context={"Tid%22:%2260b6ee4f-43c2-4c1f-b509-d6fad245297a","Oid%22:%228a735a4b-83eb-4320-997f-2d3e01fa7d95"}',
                    'id': '', 'pass': ''},
                '14:40': {
                    'link': 'https://teams.microsoft.com/l/meetup-join/19:rWPbV6_vOw8UfOuxKfASaeFON_GjUhrmA3wzA9i22y81@thread.tacv2/1635251280135?context={"Tid%22:%2260b6ee4f-43c2-4c1f-b509-d6fad245297a","Oid%22:%228a735a4b-83eb-4320-997f-2d3e01fa7d95"}',
                    'id': '', 'pass': ''},
                '16:20': {
                    'link': 'https://teams.microsoft.com/l/meetup-join/19:rWPbV6_vOw8UfOuxKfASaeFON_GjUhrmA3wzA9i22y81@thread.tacv2/1635251280135?context={"Tid%22:%2260b6ee4f-43c2-4c1f-b509-d6fad245297a","Oid%22:%228a735a4b-83eb-4320-997f-2d3e01fa7d95"}',
                    'id': '', 'pass': ''}}
        },
        '3821Б1ФИ2': {
            'Алгебра и геометрия': {'link': '', 'id': '', 'pass': ''}
        },
        '3821Б1ФИ3': {
            'Основы программирования': {'link': '', 'id': '', 'pass': ''},
            'Алгебра и геометрия': {'link': '', 'id': '', 'pass': ''},
            'Практикум по математическому анализу': {'link': '', 'id': '', 'pass': ''}
        },
        '3821Б1ФИ4': {
            'Основы программирования': {'link': '', 'id': '', 'pass': ''},
            'Практикум по математическому анализу': {'link': '', 'id': '', 'pass': ''}
        },
        '3821Б1ФИ5': {
            'Алгебра и геометрия': {'link': '', 'id': '', 'pass': ''},
            'Основы программирования': {
                '14:40': {'link': '', 'id': '', 'pass': ''},
                '16:20': {'link': '', 'id': '', 'pass': ''}},
        }
    },
    'Пт': {
        '3821Б1ФИ1': {
            'Практикум по математическому анализу': {
                'link': 'https://us04web.zoom.us/j/76741847077?pwd=MjNMQkllU1Q0eUR6Mm9WQ3NxVGJ6Zz09',
                'id': '767 4184 7077', 'pass': 'MMce1u'},
            'Алгебра и геометрия': {'link': 'https://us04web.zoom.us/j/2685906294?pwd=WGFwZ0h4T2drZ3dhRkRKc00wZjNFZz09',
                                    'id': '268 590 6294', 'pass': 'gy2Ugd'}
        },
        '3821Б1ФИ2': {
            'Основы программирования': {'link': '', 'id': '', 'pass': ''},
            'Практикум по математическому анализу': {'link': '', 'id': '', 'pass': ''},
            'Дискретная математика': {'link': '', 'id': '', 'pass': ''}

        },
        '3821Б1ФИ3': {
            'Основы программирования': {
                '07:30': {'link': '', 'id': '', 'pass': ''},
                '09:10': {'link': '', 'id': '', 'pass': ''}},
            'Дискретная математика': {'link': '', 'id': '', 'pass': ''},
            'Практикум по математическому анализу': {'link': '', 'id': '', 'pass': ''},
            'Алгебра и геометрия': {'link': '', 'id': '', 'pass': ''}
        },
        '3821Б1ФИ4': {
            'Алгебра и геометрия': {'link': '', 'id': '', 'pass': ''},
            'Практикум по математическому анализу': {'link': '', 'id': '', 'pass': ''}
        },
        '3821Б1ФИ5': {
            'Дискретная математика': {'link': '', 'id': '', 'pass': ''},
        }
    }
}


def f_chat(table, *params):
    chat = table.copy()
    for i in params:
        if i in chat.keys():
            chat = chat[i]
    try:
        return 'Ссылка на конференцию: {link}\n' \
               'Идентификатор конференции: {id}\n' \
               'Код доступа: {pass}'.format(**chat)
    except Exception:
        return 'Ссылка на конференцию: ' + randRR()


def web(day, lesson, beginLesson, kindOfWork, group):
    if kindOfWork == 'Лекция':
        return f_chat(webs_lecture, day, lesson, beginLesson, kindOfWork)
    else:
        # return f_chat(webs_practice, day, group, lesson, beginLesson, kindOfWork)
        return ''

from time import time
from pytube import Playlist

def randRR():
    link = Playlist('https://www.youtube.com/playlist?list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p')
    n = int(time())%(link.length)
    return link.video_urls[n]

webs_lecture = { 
    'ПН': {
        'Линейное программирование': 'https://events.webinar.ru/unn/12249589',
        'Математический анализ': 'https://events.webinar.ru/unn/2104097528',
        'Архитектура вычислительных систем': 'https://teams.microsoft.com/l/meetup-join/19%3ameeting_YTg1ZjAzOTAtYjViOC00NDgyLWExMjktMjAzMWQ0M2VkNDI4%40thread.v2/0?context=%7b%22Tid%22%3a%2260b6ee4f-43c2-4c1f-b509-d6fad245297a%22%2c%22Oid%22%3a%22d7978a7b-8cfe-4c39-86ac-7e14a9d1bbc2%22%7d',
        'Дифференциальные уравнения': 'https://events.webinar.ru/unn/1959671208/stream-new/377301875',
        'Алгоритмы и структуры данных': 'https://teams.microsoft.com/l/meetup-join/19%3ameeting_MmIyMTdiNDktMGRhNy00N2Q3LTg5ZGMtNjA3Y2E3NzYxMWUz%40thread.v2/0?context=%7b%22Tid%22%3a%2260b6ee4f-43c2-4c1f-b509-d6fad245297a%22%2c%22Oid%22%3a%225296e582-edba-4b94-ba1f-ca426c653e15%22%7d',
        'Безопасность жизнедеятельности': 'https://teams.microsoft.com/l/meetup-join/19%3ameeting_NjU2NDg4ODktYWI2Ni00YTlmLTk2YzktOWM4ZjM0NDFkYjIy%40thread.v2/0?context=%7b%22Tid%22%3a%2252f42523-f018-46d5-8d79-dd35c5f57d73%22%2c%22Oid%22%3a%226e9abfba-8dc6-44e7-851d-830d575ee39e%22%7d'
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
    return chat


def outChat(chat):
    # try:
    #     return 'Ссылка на конференцию: {link}\n' \
    #            'Идентификатор конференции: {id}\n' \
    #            'Код доступа: {pass}'.format(**chat)
    # except Exception:
    #     try:
    #         return 'Ссылка на конференцию: ' + randRR()
    #     except Exception:
    #         return 'Ссылка на конференцию: ' + 'https://vk.com/a_xyenno'
    return 'Ссылка на конференцию: ' + chat if 'https' in chat else randRR()


def web(day, lesson, beginLesson, kindOfWork, group):
    if kindOfWork == 'Лекция':
        table = webs_lecture
        chat = f_chat(webs_lecture, day, lesson, beginLesson, kindOfWork)
        return outChat(chat)
    else:
        return ''

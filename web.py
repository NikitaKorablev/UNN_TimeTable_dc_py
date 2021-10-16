webs_lecture = {  # одинаково у всех (все лекции)
    'Пн': {
        'Математический анализ': {'link': 'https://zoom.us/j/92825618536?pwd=NkUrbWxiTmlNQkRKVjQ',
                                  'id': '928 2561 8536', 'pass': '559912'},
        'Основы программирования': {
            '09:10': {'link': 'https://teams.microsoft.com/l/meetup-j...QwNWE1O',
                      'id': '', 'pass': ''},
            '14:40': {'link': 'https://teams.microsoft.com/l/meetup-j...RiMmNjM',
                      'id': '', 'pass': ''}},
        'Алгебра и геометрия': {'link': 'https://zoom.us/j/4282336398?pwd=RmpJM...Z3bHlmQT09',
                                'id': '428 233 6398', 'pass': '123456'}
    },
    'Ср': {
        'Эффективные алгоритмы и структуры данных-1': {'link': '', 'id': '', 'pass': ''},
        'Физическая культура и спорт (элективная дисциплина)': {'link': '', 'id': '', 'pass': ''}
    },
    'Чт': {
        'Введение в проектную деятельность': {  # это список лекций. практика по ввд будет отдельно
            'link': 'https://us02web.zoom.us/j/89480339991?pwd=c0NjcllNWWMrTC9WMlh4YWZJT1VZUT09',
            'id': '894 8033 9991', 'pass': '838968'},
        'Математический анализ': {'link': 'https://zoom.us/j/98478027286?pwd=ZDRnZ1lvOWt0TDhGMGY',
                                  'id': '984 7802 7286', 'pass': '504739'},
        'Дискретная математика': {'link': 'https://zoom.us/j/96239360433?pwd=amZBaTdBazYrYW03cDJzMHpOMHk0QT09',
                                  'id': '962 3936 0433', 'pass': '123456'}
    }
}
webs_practice = {
    'Вт': {
        '3821Б1ФИ1': {
            'Алгебра и геометрия': {'link': 'https://us04web.zoom.us/j/2685906294?pwd=WGFwZ0h4T2drZ3dhRkRKc00wZjNFZz09',
                                    'id': '268 590 6294', 'pass': 'gy2Ugd'},
            'Дискретная математика': {'link': '', 'id': '', 'pass': ''}
        },
        '3821Б1ФИ2': {

        },
        '3821Б1ФИ3': {

        },
        '3821Б1ФИ4': {

        },
        '3821Б1ФИ5': {

        }
    },
    'Ср': {
        '3821Б1ФИ1': {
            'Математический анализ': {
                'link': 'https://us04web.zoom.us/j/76741847077?pwd=MjNMQkllU1Q0eUR6Mm9WQ3NxVGJ6Zz09',
                'id': '767 4184 7077', 'pass': 'MMce1u'}
        },
        '3821Б1ФИ2': {

        },
        '3821Б1ФИ3': {

        },
        '3821Б1ФИ4': {

        },
        '3821Б1ФИ5': {

        }
    },
    'Пт': {
        '3821Б1ФИ1': {
            'Математический анализ': {
                'link': 'https://us04web.zoom.us/j/76741847077?pwd=MjNMQkllU1Q0eUR6Mm9WQ3NxVGJ6Zz09',
                'id': '767 4184 7077', 'pass': 'MMce1u'},
            'Алгебра и геометрия': {'link': 'https://us04web.zoom.us/j/2685906294?pwd=WGFwZ0h4T2drZ3dhRkRKc00wZjNFZz09',
                                    'id': '268 590 6294', 'pass': 'gy2Ugd'}
        },
        '3821Б1ФИ2': {

        },
        '3821Б1ФИ3': {

        },
        '3821Б1ФИ4': {

        },
        '3821Б1ФИ5': {

        }
    }
}


def f_chat(table, *params):
    chat = table.copy()
    for i in params:
        if i in chat.keys():
            chat = chat[i]
    return 'Ссылка на конференцию: {link}\n' \
           'Идентификатор конференции: {id}\n' \
           'Код доступа: {pass}'.format(**chat)

def web(day, lesson, beginLesson, kindOfWork):
    if kindOfWork == 'Лекция' or 'проект' in lesson or 'Физ' in lesson:
        return f_chat(webs_lecture,day,lesson,beginLesson,kindOfWork) #всё, что есть, но в нужном порядке
    else:
        return f_chat({'link': '', 'id': '', 'pass': ''})


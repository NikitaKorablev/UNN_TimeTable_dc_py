webs = {'Пн': {
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
    'Вт': {
        'Алгебра и геометрия': {'link': 'https://us04web.zoom.us/j/2685906294?pwd=WGFwZ0h4T2drZ3dhRkRKc00wZjNFZz09',
                                'id': '268 590 6294', 'pass': 'gy2Ugd'},
        'Дискретная математика': {'link': '', 'id': '', 'pass': ''}
    },
    'Ср': {
        'Математический анализ': {'link': 'https://us04web.zoom.us/j/76741847077?pwd=MjNMQkllU1Q0eUR6Mm9WQ3NxVGJ6Zz09',
                                  'id': '767 4184 7077', 'pass': 'MMce1u'},
        'Основы программирования': {
            '09:10': {'link': '', 'id': '', 'pass': ''},
            '14:40': {'link': '', 'id': '', 'pass': ''},
            '16:20': {'link': '', 'id': '', 'pass': ''}},
    },
    'Чт': {
        'Введение в проектную деятельность': {
            'Лекция': {'link': '', 'id': '', 'pass': ''},
            'Практика': {'link': '', 'id': '', 'pass': ''}},
        'Математический анализ': {'link': 'https://zoom.us/j/98478027286?pwd=ZDRnZ1lvOWt0TDhGMGY',
                                  'id': '984 7802 7286', 'pass': '504739'},
        'Дискретная математика': {'link': 'https://zoom.us/j/96239360433?pwd=amZBaTdBazYrYW03cDJzMHpOMHk0QT09',
                                  'id': '962 3936 0433', 'pass': '123456'}
    },
    'Пт': {
        'Математический анализ': {'link': 'https://us04web.zoom.us/j/76741847077?pwd=MjNMQkllU1Q0eUR6Mm9WQ3NxVGJ6Zz09',
                                  'id': '767 4184 7077', 'pass': 'MMce1u'},
        'Алгебра и геометрия': {'link': 'https://us04web.zoom.us/j/2685906294?pwd=WGFwZ0h4T2drZ3dhRkRKc00wZjNFZz09',
                                'id': '268 590 6294', 'pass': 'gy2Ugd'}
    }
}


def web(day, lesson, beginLesson, kindOfWork):
    if lesson == 'Введение в проектную деятельность':
        chat = ''
    elif lesson == 'Основы программирования':
        chat = 'Ссылка на конференцию: ' + webs[day][lesson][beginLesson]['link']
    else:
        chat = 'Ссылка на конференцию: {link}\n' \
               'Идентификатор конференции: {id}\n' \
               'Код доступа: {pass}'.format(**webs[day][lesson])
    return chat

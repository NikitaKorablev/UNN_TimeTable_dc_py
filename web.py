math_analysis = 'Математический анализ'
base_programming = 'Основы программирования'
philosophy = 'Введение в проектную деятельность'
disk = 'Дискретная математика'
algebra = 'Алгебра и геометрия'

webs = {'Пн': {
    math_analysis: {'link': 'https://zoom.us/j/92825618536?pwd=NkUrbWxiTmlNQkRKVjQ',
                    'id': '928 2561 8536', 'pass': '559912'},
    base_programming: {
        '09:10': {'link': 'https://teams.microsoft.com/l/meetup-j...QwNWE1O',
                  'id': '', 'pass': ''},
        '14:40': {'link': 'https://teams.microsoft.com/l/meetup-j...RiMmNjM',
                  'id': '', 'pass': ''}},
    algebra: {'link': 'https://zoom.us/j/4282336398?pwd=RmpJM...Z3bHlmQT09',
              'id': '428 233 6398', 'pass': '123456'}

},
    'Чт': {
        philosophy: {
            'Лекция': {'link': '', 'id': '', 'pass': ''},
            'Практика': {'link': '', 'id': '', 'pass': ''}},
        math_analysis: {'link': 'https://zoom.us/j/98478027286?pwd=ZDRnZ1lvOWt0TDhGMGY',
                        'id': '984 7802 7286', 'pass': '504739'},
        disk: {'link': 'https://zoom.us/j/96239360433?pwd=amZBaTdBazYrYW03cDJzMHpOMHk0QT09',
               'id': '962 3936 0433', 'pass': '123456'}
    }}


def web(day, lesson, kindOfWork, beginLesson):
    # print(lesson)
    chat = 0
    if lesson != 'Введение в проектную деятельность' and lesson != 'Основы программирования':
        chat = webs[day][lesson]
    elif lesson == 'Введение в проектную деятельность':
        chat = webs[day][lesson][kindOfWork]
    elif lesson == 'Основы программирования':
        chat = webs[day][lesson][beginLesson]
        # pass

    if lesson == 'Основы программирования':
        chat = 'Ссылка на конференцию: ' + str(chat['link'])
        # print(chat + '\n')
    else:
        chat = 'Ссылка на конференцию: ' + str(chat['link']) + '\n' + \
               'Идентификатор конференции: ' + str(chat['id']) + '\n' + \
               'Код доступа: ' + str(chat['pass'])
        # print(chat + '\n')

    print('something')
    return chat

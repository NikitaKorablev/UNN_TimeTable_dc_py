


"""def time_posting(std_time,ask_day):

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

    # send_message(f'Time posting: days: {day}; hours: {h}; minutes: {m}; seconds: {sec}')

    return time_before_next_posting


    # tp = time_posting(std_time='20:00')
    # time.sleep(tp)



    """

"""
if not get_post_info(date_now, date_next_d, 'today'):
    for i, j in enumerate(channels):
        table = timetable(groups[i], date_now)
        channel = client.get_channel(j)
        await channel.purge()

        if table:
            for message in table_chat(table, date_now):
                await channel.send(message)
                # pass
    set_post_info(date_now, date_next_d, 'today')
    print('Расписание на сегодня отправлено')
    send_message('Расписание на сегодня отправлено')

if not get_post_info(date_now, date_next_d, 'next day'):
    if int(time_now.split(':')[0]) >= HOUR:
        for i, j in enumerate(channels):
            table = timetable(groups[i], date_next_d)
            channel = client.get_channel(j)
            await channel.purge()
            if table:
                for message in table_chat(table, date_next_d):
                    await channel.send(message)
                    # pass
        set_post_info(date_now, date_next_d, 'next day')
        print('Расписание на завтра отправлено')
        send_message('Расписание на завтра отправлено')
    else:
        tp = time_posting([HOUR, 0, 0], time_now, 'today')
        print(f'I sleep {tp} sec')
        send_message(f'I sleep {tp} sec')
        time.sleep(tp)
else:
    tp = time_posting([HOUR, 0, 0], time_now, 'next day')
    print(f'I sleep {tp} sec')
    send_message(f'I sleep {tp} sec')
    time.sleep(tp)
"""

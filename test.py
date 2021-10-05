


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
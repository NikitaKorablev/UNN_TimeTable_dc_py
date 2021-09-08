import datetime

now_d = datetime.datetime.now()
next_day = now_d + datetime.timedelta(days=1)
# hours_next_day, minutes_next_day, _ = list(map(int, str(next_day).split()[1].split(':')))
next_day = list(map(int, str(next_day).split()[0].split('-')))
next_day = datetime.datetime(*next_day, 20, 0, 0)

time_before_next_posting = next_day - now_d

print(time_before_next_posting)
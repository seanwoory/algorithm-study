import datetime
now = datetime.datetime.now()
current_time = now.strftime(f'%Y-%m-%d')
print(current_time)
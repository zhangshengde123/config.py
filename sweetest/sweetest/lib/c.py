import datetime,time


# write your function this file
def today():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')

def now():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def unix_time():
    unix_time = time.time()
    return unix_time



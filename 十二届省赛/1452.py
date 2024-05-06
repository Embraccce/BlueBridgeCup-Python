import datetime
print((datetime.datetime(year=1970, month=1, day=1) + int(input()) * datetime.timedelta(milliseconds=1)).strftime('%H:%M:%S'))

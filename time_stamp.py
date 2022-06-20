from datetime import datetime

def get_time_stamp():
    hour = str(datetime.now().hour)
    minute = str(datetime.now().minute)
    secound = str(datetime.now().second)
    mili_secound = str(round((datetime.now().microsecond)/1000, 2))
    return hour + ":" + minute + ":" + secound + ":" + mili_secound
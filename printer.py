import datetime
import pytz
def start():
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print('test start:  %s ' % start_ts_pst)

def end():
    stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print("-------------RESULTS  -------------------------------------------")
    print('test end  :  %s' % stop_ts_pst)
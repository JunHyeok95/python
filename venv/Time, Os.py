import time
import datetime as dt

now_dt = dt.datetime.now() # 현재 시간
print(now_dt)

time.sleep(5) # 5초간 딜레이

now = time.localtime() # 기기 시간
print(now)
print(now.tm_hour)
print(now.tm_min)
print(now.tm_sec)

# insert time check
now = time.localtime()
nowTime = [now.tm_hour, now.tm_min, now.tm_sec]
print("현재 시간 - ",nowTime[0],":",nowTime[1],":",nowTime[2])
time.sleep(5)
now = time.localtime()
nowTime2 = [now.tm_hour, now.tm_min, now.tm_sec]
print("현재 시간 - ",nowTime2[0],":",nowTime2[1],":",nowTime2[2])

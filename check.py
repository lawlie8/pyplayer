import sys
import time
import datetime
file = open('xs.txt','w+')
data = {"version":"1.0","platform":sys.platform,"author":"lawlie8","last_modified":str(datetime.date.today())+"/"+time.strftime("%H:%M:%S",time.localtime())}
file.write(str(data))

import subprocess
import datetime
import time
import tg
import threading
import config
class mains(threading.Thread):
    def run(self):
        print('Alert system ON')
        while 1:
            if config.tgsend == True:
                mes = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
                output = subprocess.check_output(['last', '-n','1'])
                out = str(output).split(" ")
                user = out[0]
                user = out[0].replace(user[0] + user[1], '')
                i = 0
                for m in mes:
                    i = i + 1
                    now = datetime.datetime.now()
                    day = now.strftime("%d")#Узнаем день
                    mouth = now.strftime("%m")#Месяц
                    times = now.strftime("%H:%M")
                    if m == str(out[17]):
                        if  int(mouth) == i and times == out[19] and int(day) == int(out[18]):
                            tg.alert(text="Auth done \n" + "User: " + user + "\nIP: " + out[13] + "\n")
                            time.sleep(60)
                            break
            time.sleep(1)

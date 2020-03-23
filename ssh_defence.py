import subprocess
import os
import datetime
import threading
import db
import time
import config
import tg
import report
def alerts(number,user,ip):
    itog = db.ssh(ip=ip)
    if itog != None and config.report_brute == True and config.tgsend == True:
        tg.alert(text="Brute detected \n" + "User: " + user + "\nIP: " + ip + "\n" + "Ban_time: " + str(itog))#Сообщаем пользователю в телеграмм что произошла аунтификация
        report.abusedb(ip=ip,code="18",comm='Bruteforce SSH')

class mains(threading.Thread):#Функция оповещения о аунтификации на сервере
    print('SSHdefence system ON')
    def run(self):#Точка запуска
        while 1:#Бесконечный цикл
            time.sleep(1)#Делаем тайминг 1 секунду что бы не нагружать ресурсы сервера
            if config.tgsend == True:#Если разрешено присылать сообщения в ТГ
                    mes = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]#Список месяцев для парсиринга
                    output = os.popen("grep sshd:auth /var/log/auth.log | tail -n 1").read()
                    out = str(output).split(" ")#Делим предложение по пробелам
                    user = out[15]#Сообщаем имя юзера который аунтифицирован
                    user = str(user).replace("user=", '') #Удаляем b''
                    host = out[13].replace("rhost=", '') #Удаляем b'
                    i = 0#Инстализируем счетчик
                    for m in mes:#Запускаем перебор месяцев
                        i = i + 1#Каждый проход счетчик увеличивается на 1
                        now = datetime.datetime.now()#Узнаем нынишнию дату
                        day = now.strftime("%d")#Узнаем день
                        mouth = now.strftime("%m")#Месяц
                        h = now.hour
                        min = now.minute
                        sec = now.second
                        if int(sec) != 0:
                            if len(str(int(sec))) > 1:
                                sec = int(sec) - 1
                            else:
                                sec = int(sec) - 1
                                sec = "0" + str(sec)
                        else:
                            sec = 59
                        times = str(h) + ":" + str(min) + ":" + str(sec)#Время в часах и минутах
                        if m == str(out[0]):
                            if  int(mouth) == i and times == out[2] and int(day) == int(out[1]): #Если число месяца равно счетчику время(В часах и минутах) равно текущему и день равен текущему дню продолжаем
                                print('trig')
                                t = threading.Thread(target=alerts, args=(1,user,host))
                                t.start()
                                break#Выходим из перебора

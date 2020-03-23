import config
import socket
import db
import threading
import report
import ban
class atackpreddssh(threading.Thread):
    def run(self):
        print("Anti look SSH on")
        sock = socket.socket()#Сообщаем о сокете
        sock.settimeout(15)#Делаем таймаут
        ssh = config.ssh_realy - 1#Ставим перед настоящим портом SSH прослушку
        sock.bind(('0.0.0.0', ssh))#Сообщаем о прослушке
        sock.listen(10)#Слушаем
        def connectingg():
            while True:
                try:
                    client, addr = sock.accept()#Если все норм принимаем подключение
                    print(addr)#Сообщаем о адресе
                    try:
                        client.send(b'SSH-2.0-OPENSSH_7.9\r\n')#Отправляем фейковый SSH
                        if config.abuse_send == True:#Если можно отправляем abuse
                            ip = str(addr[0])
                            report.abusedb(ip=ip,code='18',comm="Brute SSH")#сообщаем
                        if config.report_scan == True:
                            tg.alert(text="Обнаружено сканирование: \nIP:" + addr[0])
                        if config.ban_atacker == True:#Баним атакующего
                            try:
                                db.ban_ip(ip=addr[0])#Сообщаем БД
                                ban.ban_scan(ip=addr[0])#Баним
                                client.close()
                            except:
                                pass
                    except:
                        pass
                except:
                    pass
        main = threading.Thread(name='listening1', target=connectingg())
        main.start()

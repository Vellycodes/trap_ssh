import db
import config
import threading
import socket
import report
import ban
class atackpredssh(threading.Thread):
    def run(self):
        print('Antiscan system ON')
        sock = socket.socket()#Сообщаем о том что создается сокет
        sock.settimeout(15)#Создаем таймаут
        sock.bind(('0.0.0.0', config.one_port))#Сообщаем какой порт и адрес мы будем слушать
        sock.listen(1)#Слушаем порт
        def connectingg():#Если случилось подключение активируется эта функция
            while True:#Бесконечный цикл
                try:#Если все хорошо (1)
                    client, addr = sock.accept()#Одобряем
                    print(addr)#Публикуем IP
                    try:#Если все хорошо(2)
                        client.send(b'SSH-2.0-OPENSSH_7.9\r\n')#Сообщаем клиенту фейк SSH
                        if config.abuse_send == True:#Если в конфигах разрешена отправка в Abuseipdb
                            ip = str(addr[0])#Присваем переменной ip адрес string формата
                            report.abusedb(ip=ip,code='14',comm="Scan ports")#Сообщаем AbDIP что был просканирован порт
                        if config.report_scan == True:
                            tg.alert(text="Обнаружено сканирование: \nIP:" + addr[0])
                        if config.ban_atacker == True:#Если разрешен бан атакующих баним
                            try:#Если все хорошо (3)
                                db.ban_ip(ip=addr[0])#Запись в БД
                                ban.ban_scan(ip=addr[0])#Бан ip
                                client.close()#Закрываем подключение
                            except:#Если все плохо (3)
                                pass#Игнорим
                    except:#Если все плохо (2)
                        pass#Игнорим
                except:#Если все плохо (1)
                    pass#Игнорим
        main = threading.Thread(name='listening1', target=connectingg())#При совершении подключения сообщаем что main это поток
        main.start()#Запускаем поток

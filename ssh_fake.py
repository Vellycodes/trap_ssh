import report
import config
import db
import threading
import socket
import report
import ban
import tg
class atack22(threading.Thread):
    def run(self):
        print('FakeSSH system ON')
        #За коменты обращайтесь в antiscan.py
        sock = socket.socket()
        sock.settimeout(3)
        sock.bind(('0.0.0.0', 22))
        sock.listen(100)
        def connecting():
            while True:
                try:
                    client, addr = sock.accept()
                    print(addr)
                    try:
                        client.send(b'SSH-2.0-OPENSSH_7.9\r\n')
                        if config.abuse_send == True:
                            ip = str(addr[0])
                            report.abusedb(ip=ip,code='18',comm="honeypot 22 port")
                        if config.report_fakeSSH == True:
                            tg.alert(text="Обнаружено попадание на фейковый SSH\nIP:" + str(addr[0]))
                        if config.ban_atacker == True:
                            try:
                                db.ban_ip(ip=addr[0])
                                ban.ban_scan(ip=addr[0])
                                client.close()
                            except:
                                pass
                    except:
                        pass
                except:
                    pass

        main = threading.Thread(name='listening', target=connecting)
        main.start()

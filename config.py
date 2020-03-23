import urllib.parse
abusekey = "" #abuseipdb.com
dblogin = urllib.parse.quote_plus('')
dbpass = urllib.parse.quote_plus('')
dbname = "defence" #dbname
dbaddr = "" #db ip
tgtoken = ""# telegram.org token
tgsend = False #sending telegram
abuse_send = True #sending abuse db
ban_atacker = True #True ban ip / False retention connecting
ssh_port_fake = 22 #fake ssh
ssh_realy = 2560# realy ssh
alert_entrance = True #Оповещение о входе

#Уплавление через telegtam bot
enable_bot = False #Off bot = false , On = True
root_bot = 0 #ID user root tg

#Порты для обнаружения грубого сканирования
one_port = 465
#Настрйка банов и репортов
progress = False #Прогрессивный бан
report_scan = False#Сообщать о попытках сканирования
report_brute = False #Сообщать пользователю в ТГ о попытках брута
report_fakeSSH = False
report_SSH = False

#Настройка пределов попыток
ssh_predel = 1

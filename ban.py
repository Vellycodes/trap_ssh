import os
def ban_scan(ip):#Отвечает за бан
    os.system("sudo iptables -A INPUT -s" + ip + " -j DROP")#Баним через IPtables 

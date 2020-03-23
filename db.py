# -*- coding: utf-8 -*-
from pymongo import MongoClient
import config
import threading
import datetime
import os
import ban
#С аунтификацией
try:#Если аунтификация через пароль проходит используем ее
    client = MongoClient('mongodb://%s:%s@%s' % (config.dblogin,config.dbpass,config.dbaddr))
except:
    client = MongoClient('127.0.0.1', 27017)#Если нет
db = client[config.dbname]#Сообщаем название базы из конфига
posts = db.posts#Название таблицы
sshh = db.ssh#Название таблицы

pp = db.ports#Название таблицы
def ban_ip(ip):#Отвечает за добавление в базу IP
    print(ip)#Показываем IP
    date = datetime.datetime.now()#Узнаем дату
    p = posts.find_one({"ip": ip})#Ищем IP на рицидив
    end_date = date + datetime.timedelta(minutes=3)#Блокируем на 3 минуты
    end_datee = date + datetime.timedelta(days=1)# На 1 сутки при рецидиве
    if p == None:#Если IP не найден
        post = {"ip": ip,#Сообщаем IP
                "date": '{:%Y-%m-%d %H:%M}'.format(end_date),#Добавляем 3 минуты к бану
                "count": 0}#Попытки
        post_id = posts.insert_one(post).inserted_id#создаем запись
    else:#Если рецидив
        s = p['count']#Узнаем кол во попыток
        s = s + 1#Добовляем кол во попыток
        if config.progress == True:
            end_datee = date + datetime.timedelta(days=s * 2)# Прогрессивный бан
        db.posts.update({'ip': ip},
                        {'$set': {'date': '{:%Y-%m-%d %H:%M}'.format(end_datee), "count": s}})#Блокируем на длительное время

class unban(threading.Thread):
    def run(self):
        while 1:
            date = datetime.datetime.now() #Узнаем дату
            p = posts.find_one({"date": '{:%Y-%m-%d %H:%M}'.format(date)})#узнаем кого надо разбанить
            if p != None:#Если чел найден в это время его надо разбанить
                os.system("sudo iptables -D INPUT -s " + p['ip'] + " -j DROP")#Разбан
                print('Unbanned' + str(p['ip']))
                db.posts.update({'ip': p['ip']},
                                {'$set': {'date': 0}})#Обновляем БД

def ssh(ip):
    p = sshh.find_one({"ip":ip})#узнаем кого надо разбанить
    date = datetime.datetime.now()#Узнаем дату
    if p != None:
        end_date = date + datetime.timedelta(minutes=p['count_never'] * 2)
        db.ssh.update({'ip': ip},
                        {'$set': {'date': '{:%Y-%m-%d %H:%M}'.format(end_date), "count": p['count'] + 1}})#Блокируем на длительное время
        count_end = p['count'] + 1
        if count_end == config.ssh_predel:
            db.ssh.update({'ip': ip},
                            {'$set': {'date': '{:%Y-%m-%d %H:%M}'.format(end_date), "count": p['count'] + 1,'count_never':p['count_never'] + 1}})#Блокируем на длительное время
            ban.ban_scan(ip=ip)#Баним IP
            return  '{:%Y-%m-%d %H:%M}'.format(end_date) #Возращаем время до разбана
    else:
        end_date = date + datetime.timedelta(minutes=3)
        post = {"ip": ip,#Сообщаем IP
                    "date": '{:%Y-%m-%d %H:%M}'.format(end_date),#Добавляем 3 минуты к бану
                    "count": 1,
                    "count_never": 1}#Попытки
        post_id = sshh.insert_one(post).inserted_id#создаем запись


class unban_ssh(threading.Thread):
    def run(self):
        while 1:
            date = datetime.datetime.now() #Узнаем дату
            p = sshh.find_one({"date": '{:%Y-%m-%d %H:%M}'.format(date)})#узнаем кого надо разбанить
            if p != None:#Если чел найден в это время его надо разбанить
                os.system("iptables -D INPUT -s " + p['ip'] + " -j DROP")#Разбан
                print('Unbanned' + str(p['ip'])) #Говорим что бан снят
                db.ssh.update({'ip': p['ip']},
                                {'$set': {'date': 0,'count':0}})#Обновляем БД

import alert
import antiscan
import config
import report
import ssh_fake
import tg
import antiscan_ssh
import tg_bot
import ban
import db
import ssh_defence
import threading
alert.mains().start()
antiscan_ssh.atackpreddssh().start()
antiscan.atackpredssh().start()
ssh_fake.atack22().start()
if config.enable_bot == True:
    tg_bot.bott().start()
db.unban().start()
db.unban_ssh().start()
ssh_defence.mains().start()

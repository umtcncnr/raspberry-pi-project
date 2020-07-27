import smtplib
from average import read_file
from datetime import datetime
server="smtp.gmail.com"
port=587
user="from_mail_address"
password="from_password"
class sender():
    def __init__(self):
        pass
    def sendmail(self, recipient,subject):
        obj=read_file()
        obj.read_datas()
        temp_average=obj.temp_average
        humid_average=obj.humid_average
        time=datetime.now()
        content=time.ctime()+"\taverage temperature of the day :"+temp_average+"\naverage humidity of the day :"+humid_average
        header=["From" + user, "Subject"+subject, "To"+recipient,""]
        header="\r\n".join(header)
        session=smtplib.SMTP(server,port)
        session.ehlo()
        session.starttls()

        session.login(user,password)

        session.sendmail(user,recipient,header + content)
        session.quit()

x=sender()
sendto="to_mail_address"
subj="subject"
x.sendmail(sendto,subj)

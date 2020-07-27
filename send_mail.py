import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
server="smtp.gmail.com"
port=587
user="from_mail_addres"
password="from_password"
class sender():
    def __init__(self):
        pass

    def sendmail(self, recipient,subject):
        msg=MIMEMultipart()
        msg["subject"]=subject
        msg["from"]=user
        msg["to"]=", ".join(recipient)

        part=MIMEBase("application","octet-stream")
        part.set_payload(open("results.pdf","rb").read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition","attachment; filename='result.pdf'")

        msg.attach(part)

        session=smtplib.SMTP(server,port)
        session.ehlo()
        session.starttls()

        session.login(user,password)
        session.sendmail(user,recipient,msg.as_string())
        session.quit()

x=sender()
sendto="to_mail_address"
subj="temp and humidity info"
x.sendmail(sendto,subj)

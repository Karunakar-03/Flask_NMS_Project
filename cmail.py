import smtplib 
from email.message import EmailMessage
mail_password='kkbx praw nmeq ntig'
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('karunakarramisetti12@gmail.com',mail_password)
    msg=EmailMessage()
    msg['FROM']='karunakarramisetti12@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('msg sent')
    server.close()

import smtplib
sender='rajeshvv01@gmail.com'
receiver='veerurajesh.s@gmail.com'
password='Sweetheart@143'
smtpserver=smtplib.SMTP("smtp@gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(sender,password)
msg='Subject:Demo\nThis is a demo'
smtpserver.sendmail(sender,receiver,msg)
print('Sent')
smtpserver.close()
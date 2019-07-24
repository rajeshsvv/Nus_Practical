import smtplib
import os


# create  smtp session
s=smtplib.SMTP("smtp.gmail.com",587)

# start TLS for security
s.starttls()

try:
    user_email = os.environ.get("username")
    password = os.environ.get("password")
    # Authentication
    s.login(user_email,password)

    # Message to be sent
    message="Please Forward this content"


    # sending the mail
    s.sendmail('veerurajesh.s@gmail.com',"rajeshsvv01@gmail.com",message)

    # terminatimg the session
    s.quit()
except ValueError as e:
    e.exception
finally:
    print("close all the connection")



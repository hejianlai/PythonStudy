#!/usr/bin/python
import smtplib
import string
HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"
TO = "964287149@qq.com"
FROM = "1259525040@qq.com"
text = "Pthon rules them all!"
BODY = string.join((
    "From: %s" % FROM,
    "To:    %s" % TO,
    "Subject:   %s" % SUBJECT,
    "",
    text
    ),"\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("1259525040@qq.com","w776875@")
server.sendmail(FROM,[TO],BODY)
server.quit()
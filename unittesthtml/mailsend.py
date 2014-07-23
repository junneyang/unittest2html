#!/usr/bin/env python
#-*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

from fileLib import *


sub_str=u"测试邮件"
body_content=get_file_lines("index.html")
body_content_tmp=""
for line in body_content:
    body_content_tmp+=line

mail=MIMEMultipart()
mail["Subject"]=sub_str
body = MIMEText(body_content_tmp,'html','utf-8')
mail.attach(body)

mail["From"]="yangjun03@baidu.com"
mail["To"]="yangjun03@baidu.com"
smtp=smtplib.SMTP("mail2-in.baidu.com")
smtp.sendmail(mail["From"], mail["To"].split(","), mail.as_string())
smtp.quit()


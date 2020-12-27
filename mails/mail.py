# -*- coding: utf-8 -*-
"""mail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11lQYNsIf8fqvk4IZS4O6695baY7tNH9j
"""

#import libraries
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import imghdr
from PIL import Image
import requests
from io import BytesIO
from email.message import EmailMessage as EM
from email.utils import make_msgid

smtp_server='smtp.live.com'
port=587
sender_mail='sender mail'
sender_pass='sender\'s password'
receiver_mail='receiver mail'
context=ssl.create_default_context()
#message=EM()
asparagus_cid = make_msgid()
message = MIMEMultipart('alternative')
message["Subject"] = "Bitcoin update"
message["From"] = sender_mail
message["To"] = receiver_mail
body="""\
This was sent to you to make you up to date with Crypto-Currency!
"""
#processing image from the net
response = requests.get("https://en.wikipedia.org/wiki/Bitcoin#/media/File:Casascius_coin.jpg")
#img = Image.open(BytesIO(response.content))
im = open('Bitcoin.png','wb')
im.write(response.content)

imag=open('Bitcoin.png','rb').read()
#with open('Qt.png', 'rb') as img:
#	message.get_payload()[1].add_related(img.read(), 'image', 'png', cid=asparagus_cid)
#img = open('Qt.png','wb')
#img.write(response.content)
#with open('Qt.png','rb') as f: #for pdf
#  file_data=f.read()
#  file_type=imghdr.what(f.name)
#  file_name=f.name
#  message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
image = MIMEImage(imag,'image',name='Bitcoin.png')
text=MIMEText(body,'plain')
message.attach(text)
message.attach(image)
#connect to the server and send data
with smtplib.SMTP(smtp_server,port) as server:
  server.ehlo()
  server.starttls(context=context)
  server.ehlo()
  server.login(sender_mail,sender_pass)
  server.sendmail(sender_mail,receiver_mail,message.as_string())
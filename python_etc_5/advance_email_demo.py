#!usr/bin/env/python3

import smtplib, ssl
import os
from email.message import EmailMessage
import credentials

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
# HOST = 'smtp.gmail.com'
# PORT = 587
# context=ssl.create_default_context()

# msg = EmailMessage()
# msg['Subject'] = "Email Testing By Dominic"
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = EMAIL_ADDRESS
# msg.set_content("Is all about tesing...")

# with smtplib.SMTP(HOST, PORT) as smtp:
# 	smtp.starttls(context=context)
# 	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
# 	smtp.send_message(msg)

# data = os.getenv('EMAIL_USER')
# print(data)


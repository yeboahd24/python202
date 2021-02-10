#!usr/bin/env/python3
import smtplib
import os

#SIMPLE WAY
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
HOST = 'smtp.gmail.com'
PORT = 587
with smtplib.SMTP(HOST, PORT) as smtp:
	# smtp.ehlo() # sound
	# smtp.starttls() # encrypting traffic
	# smtp.ehlo() # sound
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

	subject = "Email Testing By Dominic"
	body = "Is all about tesing..."
	msg = f"Subject: {subject}\n\n{body}"
	smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg) # TO MYSELF


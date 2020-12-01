#!usr/bin/env/python3

# Sending max email
import smtplib
from email.mime.text import MIMEText
def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, headers=None):

	headers = {} if headers is None else headers

	email = MIMEText(message)
	email['Subject'] = subject
	email['From'] = from_addr

	for header, value in headers.items():
		email[header] = value
	sender = smtplib.SMTP(host, port)

	for addr in to_addrs:
		del email['To']
		email['To'] = addr
		sender.sendmail(from_addr, addr, email.as_string())
	sender.quit()


#Test Case:
# first run it debug mode by python -m smtpd -n -c DebuggingServer localhost:1025
send_email("A model subject", "The message contents",\
	"from@example.com", "to1@example.com", "to2@example.com")


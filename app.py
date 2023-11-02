import sys
import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

os.environ['RECIPIENT_EMAIL'] = 'francisali692@gmail.com'
os.environ['MAIL_PASSWORD'] = 'U5T3G9ZX6MLKfOdq'

from flask import Flask, render_template, request
from mail_config import mail_config


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
	sender_email = mail_config.get('MAIL_USERNAME')
	recipient_email = os.getenv('RECIPIENT_EMAIL')
	
	if request.method == 'POST':
		values = request.values
		print(values.get('name'))
		print(values.get('email'))
		print(values.get('message'))
		msg = MIMEMultipart()
		msg['From'] = mail_config.get('MAIL_USERNAME')
		msg['To'] = os.getenv('RECIPIENT_EMAIL')
		msg['Subject'] = f"E-mail from {values.get('name')}"

		body = f'''
			{values.get('message')}

			{values.get('name')}.

			
			Give a feedback to {values.get('name')} at {values.get('email')}.
			'''
		msg.attach(MIMEText(body, 'plain'))

		# Start the SMTP session
		server = SMTP(
			mail_config.get('MAIL_SERVER'), 
			mail_config.get('MAIL_PORT')
		)
		server.starttls()
		server.login(sender_email, mail_config.get('MAIL_PASSWORD'))

		server.sendmail(sender_email, recipient_email, msg.as_string())
		server.quit()
	return render_template('form.html')
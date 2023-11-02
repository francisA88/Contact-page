import sys
import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message
from mail_config import mail_config


app = Flask(__name__)
app.config.update(mail_config)

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		values = request.values
		message = Message(
			"E-mail from {values.get('name')}",
			sender = mail_config.get('MAIL_USERNAME'),
			recipients = [os.getenv("RECIPIENT_EMAIL")]
		)
		message.body = f'''
			{values.get('message')}

			My email address: {values.get('email')}.

			{values.get('name')}.
			'''
		mail.send(message)
	return render_template('form.html')
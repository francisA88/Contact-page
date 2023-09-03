import sys

from flask import Flask, render_template, request
from flask_mail import Mail, Message
from mail_config import mail_config


app = Flask(__name__)
app.config.update(mail_config)

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def main():
	questions = {
		'Q1':'School name',
		'Q2': 'Course of study',
		'Q3': 'Current year',
		'Q4': 'Did the course meet your expectations? If not, why?'
	}
	if request.method == 'POST':
		try:
			vals = request.values
			name = vals.get('name')
			email = vals.get('email')
			response = \
			f'''Thank you for taking this survey, {name}!

			Below are the details of your response:
			'''
			for Q in questions:
				ques = questions[Q]
				ans = vals.get(Q)
				response += f'{ques}: {ans}\n'
			mail_response = Message(
				'School Survey Feedback',
				sender = mail_config.get('MAIL_USERNAME'),
				recipients = [email]
			)
			if vals.get('check') == 'on':
				mail_response.body = response
				mail.send(mail_response)

			return "200"
		except Exception as e:
			print(e)
			return "500"

	return render_template('form.html')
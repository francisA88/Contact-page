import os


mail_config = {
	'MAIL_SERVER': 'smtp.gmail.com',
	'MAIL_PORT': 465,
	'MAIL_USERNAME': 'dummy42113@gmail.com',
	'MAIL_PASSWORD': os.environ.get('MAIL_PASSWORD'),
	'MAIL_USE_TLS': False,
	'MAIL_USE_SSL': True
}
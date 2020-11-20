#https://accounts.google.com/DisplayUnlockCaptcha
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from environ_set import environ_set
from templates import Templates
import os


environ_set()
#environment variables
username = os.environ['gmail_username']
password = os.environ['gmail_password']
smtphost = 'smtp.gmail.com'
port = 587


class SendEmail:

	from_email="100days_code <codepython100@gmail.com>"
	def __init__(self, subject, to_list=[], context={}, template=None, html_template=None):
		if template == None and html_template == None:
			raise Exception("you must define a template")

		assert isinstance(to_list, list)
		self.to_list = to_list
		self.subject = subject
		self.template = template
		self.context = context
		self.html_template = html_template

	def format_msg(self):
		msg = MIMEMultipart('alternative')
		msg['From'] =  SendEmail.from_email
		msg['To'] =",".join(self.to_list)
		msg['Subject']= self.subject

		if self.template != None:
			temp_str = Templates(template_name = self.template, context = self.context)
			txt_part= MIMEText(temp_str.render(), 'plain')
			print(txt_part)
			msg.attach(txt_part)
		if self.html_template != None:
			temp_str = Templates(template_name = self.html_template, context = self.context)
			html_part= MIMEText(temp_str.render(), 'html')
			msg.attach(html_part)
		msg_str = msg.as_string()
		return	msg_str

	def send_mail(self):
		msg =  self.format_msg()

		with smtplib.SMTP(smtphost, port) as server:
			server.ehlo()
			server.starttls()
			c=server.login(username, password)
			print(c)
			sent = False
			try:
				server.sendmail(self.from_email, self.to_list, msg)
				sent = True
			except NameError as ne:
				print(ne)
				sent = False

		return sent


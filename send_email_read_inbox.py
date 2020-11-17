#https://accounts.google.com/DisplayUnlockCaptcha
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from environ_set import environ_set
import os


environ_set()
#environment variables
username = os.environ['gmail_username']
password = os.environ['gmail_password']
smtphost = 'smtp.gmail.com'
port = 587

def send_email_read_inbox(text='first email from python', from_email="100days_code <codepython100@gmail.com>", subject="Hello World", to_list=None, html=None ):

		assert isinstance(to_list, list)

	#with smtplib.SMTP(smtphost, port) as smtp:
		smtp  = smtplib.SMTP(smtphost, port)

		smtp.ehlo()
		smtp.starttls()

		smtp.login(username, password)

		msg = MIMEMultipart('alternative')
		msg['From'] =  from_email
		msg['To'] =",".join(to_list)
		msg['Subject']= subject

	
		txt_part= MIMEText(text, 'plain')
		msg.attach(txt_part)

		if html !=None:
			html_part= MIMEText("<h1>this is working</h1>", 'html')
			msg.attach(html_part)

		msg_str = msg.as_string()

		try:
			smtp.sendmail(from_email, to_list, msg_str)
			sent = True
		except:
				sent = false

		print(sent)
		smtp.quit()
		









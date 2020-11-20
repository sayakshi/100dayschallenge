import imaplib
from imaplib import IMAP4_SSL
import email


from environ_set import environ_set
import os


environ_set()
#environment variables
username = os.environ['gmail_username']
password = os.environ['gmail_password']
smtphost = 'smtp.gmail.com'
port = 587

def read_inbox():

	with IMAP4_SSL('imap.gmail.com') as mail:

		mail.login(username, password)
		_, get_msg_count = mail.select('INBOX')
		print(f"total msgs in INBOX: {get_msg_count[0].decode()}")

		_, search_data = mail.search(None, 'ALL')
		for num in search_data[0].split():		
			_, data = mail.fetch(num, '(RFC822)')
			_, b = data[0]
			email_message = email.message_from_bytes(b)
			for header in ['subject', 'from', 'to']:
				print("{}: {}".format(header, email_message[header]))
				for msg in email_message.walk():
					print(msg.get_payload(decode=True))
			print("=============================================")




       



if __name__=="__main()__":
	read_inbox()














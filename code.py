from fedora.client.fas2 import AccountSystem
from fedora.client import AuthError
import sys
import getpass

def get_email():
	uid = raw_input("Enter the username you wish to search> ") 
	fas = AccountSystem(username=str(USERNAME), password=str(PASSWORD))
	value = fas.people_by_key(key='email', search=uid, fields=['email'])
	email_id = value.keys()
	if str(email_id)[12:][:-3] == '':
		print ("No email id associated to this account")
	else:
		print ("Email id to the user " + str(uid) + " is " +str(email_id)[12:][:-3])
	sys.exit()

def main():
	global USERNAME
	USERNAME = raw_input("Enter you FAS username> ")
	global PASSWORD
	PASSWORD = getpass.getpass("Enter your FAS pasword> ") 
	get_email()

main()

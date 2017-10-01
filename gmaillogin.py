import ctypes
import imaplib
import email
import getpass
mail = imaplib.IMAP4_SSL('imap.gmail.com')
username=raw_input("Please enter your username")
pwd=getpass.getpass("Please enter your password")
mail.login(username,pwd)
mail.list()
mail.select('inbox')

    

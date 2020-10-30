import imaplib
import base64
import os
import email

email_user = ("parthi.poo@gmail.com")
email_pass = ("")

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email_user,email_pass)
mail.select()

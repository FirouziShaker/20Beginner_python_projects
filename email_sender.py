#go over to our gmail account and setup 2 factor authentication
# generate app password
# create a function to send the email


from email.message import EmailMessage
#from app2 import password
import ssl
import smtplib

email_sender= input("Please enter your email: ")
password= input("Please enter your password: ")
email_password= password

email_reciever = input("Please enter the email of reciever : ")

subject = "Dont forget to learn more "
body= """
when you watch a video , please
"""

em = EmailMessage()
em['From'] = email_sender
em['TO'] = email_reciever
em['subject'] = subject
em.set_content(body)

context= ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com' , 465 , context=context) as smtp:
    smtp.login(email_sender , email_password)
    smtp.sendmail(email_sender, email_reciever,em.as_string())
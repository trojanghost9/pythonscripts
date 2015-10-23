import smtplib

# Sends email report
sender = 'fromemail@email.tld'
receivers = ['email2@email.tld', 'email1@email.tld']

message = """From: name <fromemail@email.tld>
To: name <'toemail@email.tld'>
Subject: The subject should go here.

The Body should go here
 """

try:
    smtpObj = smtplib.SMTP('mail.comicsn.beer')
    smtpObj.login("email@someemail.tld", "somepassword")
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
except:
    print "Error: unable to send email"



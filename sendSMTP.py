# Import smtplib for the actual sending function
import smtplib
import getpass
# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open('sendSMTP.py', 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

me = 'chandlergriscom@letu.edu'
you ='brianhowell@letu.edu'
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'SMTPLIB WORKS!'
msg['From'] =me 
msg['To'] = you 


pwd = getpass.getpass()

s = smtplib.SMTP('smtp.office365.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(me,pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()




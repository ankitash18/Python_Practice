import smtplib
from email.message import  EmailMessage

email = EmailMessage()
email['subject'] ='Test Mail form Python'
email['From']  ='shri.anki@gmail.com'
email['To'] = 'shri.anki@mgial.com'
email_content ='HI'
email.set_content(email_content)


conn = smtplib.SMTP('smtp.gmail.com',587) #connection object

#onn.ehlo()

conn.starttls()

conn.login('shri.anki@gmail.com','ankita181288')
conn.send_message(email)
conn.quit()
#conn.sendmail('shri.anki@gmail.com','shri.anki@gmail.com','Subject:So long..\n\n')



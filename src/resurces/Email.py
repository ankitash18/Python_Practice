import smtplib


conn = smtplib.SMTP('smtp.gmail.com',587) #connection object

conn.ehlo()

conn.starttls()

conn.login('shri.anki@gmail.com','ankita181288')
conn.sendmail('shri.anki@gmail.com','shri.anki@gmail.com','Subject:So long..\n\n')



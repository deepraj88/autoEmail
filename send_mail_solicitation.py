#!/usr/bin/python -tt
import sys

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email.mime.multipart import MIMEMultipart
from datetime import date
import smtplib
import pandas as pd

SMTP_SERVER = "smtp.gmail.com"
#SMTP_SERVER = "smtp.nyu.edu"
SMTP_PORT = 587
#SMTP_PORT = 465
SMTP_USERNAME = "sender@nyu.edu"
#SMTP_USERNAME = "sender@gmail.com"
SMTP_PASSWORD ="password"

#EMAIL_TO = ["receiver@gmail.com"]
EMAIL_FROM = "sender@nyu.edu"
#EMAIL_FROM = "sender@gmail.com"
EMAIL_SUBJECT = "CSAW Paper Submission"

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

INIT=""

def send_email(emailTo, emailSubject, emailBody):
    msg = MIMEMultipart('aleternative')
    part1 = MIMEText(emailBody, 'html')
    #part1 = MIMEText(emailBody, 'text')
    #part2 = MIMEText(CORE, 'html')
    msg.attach(part1)
    #msg.attach(part2)
    msg['Subject'] = emailSubject #+ " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = emailTo #EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, emailTo, msg.as_string())
    #mail.sendmail("sonideepraj@gmail.com", "sonideepraj@gmail.com", "This is a message.")
    mail.quit()

df = pd.read_csv(sys.argv[1], usecols=[int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])], names=["paper", "email","name"],na_values=["not available", "n.a."])
df = df[df['email'].notna()]
df = df[df['name'].notna()]
print(df)
for index, row in df.iterrows():
    if(index == 0):
        continue
    print(row['email'], row['name'], row['paper'])
    INIT = "Hi " + row['name'] + ","
    print(INIT)
    CORE="""\
    <html>
      <head></head>
      <body>
      <p>
    Dear {name},<br>
    <br>
    My name is Deepraj Soni and I am writing to you on behalf of the <b>NYU</b> organizing committee.<br>
    <br>
    Thank you,<br>
    <br>
    Deepraj Soni <br>
    Ph.D. Candidate and CSAW Co-Chair <br>
    NYU Tandon School of Engineering & <a href=https://cyber.nyu.edu/>NYU Center for Cybersecurity</a><br>
    csaw-research@nyu.edu<br>
    <br>
    <br>
        </p>
      </body>
    </html>
    """.format(name=row['name'], code=row['paper'])

    send_email(row['email'], EMAIL_SUBJECT, CORE) 

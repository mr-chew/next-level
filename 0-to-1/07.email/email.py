import smtplib
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email_config import gmail_pass, user, host, port

def send_email_attach(to, subject, body):
    # create message object
    message = MIMEMultipart()
    
    # add the header
    message['From'] = Header(user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject)
    
    # attach nessage body as MIMEText
    message.attach(MIMEText(body,'plain', 'utf-8'))

    data_folder = Path("data/")
    file_to_open = data_folder / "sample.txt"
    f = open(file_to_open, 'rb')
    att = MIMEApplication(f.read(), _subtype="txt")
    att.add_header('Content-Disposition', f"attachment'; filename={Path(file_to_open).name}")
    message.attach(att)

    # setup email server
    server = smtplib.SMTP_SSL(host, port)
    server.login(user,gmail_pass)

    # send email and quit server
    server.sendmail(user, to, message.as_string())
    server.quit()
    
# who are we sending this email to?
to = "******@******.com"
 
# what is our subject line?
subject = "An example email"
 
# what is the body of the email?
body = "Hi,\nThis email is an example of how to send emails in Python\nRegards"
 
send_email_attach(to, subject, body)
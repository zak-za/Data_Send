import smtplib
from email.mime.text import MIMEText
import os


def send_mail(body):
    sender_email = os.environ.get("SENDER_EMAIL") 
    sender_password = os.environ.get("PASS_WORD") 
    for recipient_email in os.environ.get("RECIPIENT_EMAILS").split(','):
        
        # recipient_cc="najlae.sebbar@emeal.nttdata.com"
        subject = "Daily Jobs Mail"
        html_message = MIMEText(body, 'html')
        html_message['Subject'] = subject
        html_message['From'] = sender_email
        html_message['To'] = recipient_email

        try:
            smtpObj = smtplib.SMTP('smtp.office365.com', 587)
        except Exception as e:
            print(e)
            smtpObj = smtplib.SMTP_SSL('smtp.office365.com', 465)

        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(sender_email, sender_password)
        smtpObj.sendmail(sender_email, recipient_email,  html_message.as_string())

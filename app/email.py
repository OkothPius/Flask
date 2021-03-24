from flask_mail import Mail, Message
from app import mail

class SendMail:
    def send_email(to, subject, sender, recipients, text_body, html_body):
        msg = Message('Hello', sender='orukopius8@gmail.com', recipients=['christinemoyo@gmail.com'])
        msg.body = "This is the email body"
        mail.send(msg)

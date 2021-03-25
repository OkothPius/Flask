from flask import current_app
from flask_mail import Mail, Message
from app import mail
from threading import Thread

class SendMail:

    def send_async_email(app, msg):
        with app.app_context():
            mail.send(msg)

    def send_email(subject, sender, recipients, text_body, html_body):
        msg = Message('Hello', sender='orukopius8@gmail.com', recipients=['christinemoyo@gmail.com'])
        msg.body = "This is the email body"
        msg.html = html_body
        # Thread(target = send_async_email, args=(current_app._get_current_object(), msg)
        mail.send(msg)


from flask import current_app
from flask_mail import Message
from app import mail
from threading import Thread


def send_async_email(self, app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(self, subject, sender, recipients, text_body, html_body, attachments=None, sync=False):
    msg = Message('Hello', sender='orukopius8@gmail.com', recipients=['okoth.ogutu@students.ku.ac.ke'])
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = "This is the email body"
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        Thread(target = send_async_email,
                 args=(current_app._get_current_object(), msg)).start()


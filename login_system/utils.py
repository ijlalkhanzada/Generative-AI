import re
from flask_mail import Mail, Message
from app import app

mail = Mail(app)

def validate_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def send_reset_email(to_email):
    msg = Message('Password Reset', sender='noreply@example.com', recipients=[to_email])
    msg.body = 'Click the link to reset your password: http://127.0.0.1:5000/reset-password'
    mail.send(msg)

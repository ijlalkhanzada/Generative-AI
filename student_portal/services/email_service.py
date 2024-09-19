# services/email_service.py

from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message, Mail

mail = Mail()

def send_verification_email(email):
    token = generate_token(email)
    msg = Message('Verify your email', recipients=[email])
    msg.body = f'Click the link to verify your account: {url_for("verify_email", token=token, _external=True)}'
    mail.send(msg)

def generate_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='email-confirm-salt')

@app.route('/verify_email/<token>')
def verify_email(token):
    try:
        email = confirm_token(token)
        # Set the student as verified in the database
        flash('Your account has been verified', 'success')
        return redirect(url_for('login'))
    except:
        flash('The verification link is invalid or has expired.', 'danger')
        return redirect(url_for('signup'))

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import os

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'your_mailtrap_username'
app.config['MAIL_PASSWORD'] = 'your_mailtrap_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Serializer for token generation
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# User Model
class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(int(student_id))

# Forms
class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

# Routes
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Create new student and save to DB
        student = Student(email=email, password=hashed_password)
        db.session.add(student)
        db.session.commit()
        
        # Send verification email
        token = serializer.dumps(email, salt='email-confirm-salt')
        send_verification_email(email, token)
        
        flash('A verification email has been sent to your email address.', 'info')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        student = Student.query.filter_by(email=form.email.data).first()
        if student and bcrypt.check_password_hash(student.password, form.password.data):
            if student.is_verified:
                login_user(student)
                return redirect(url_for('student_portal'))
            else:
                flash('Please verify your email before logging in.', 'warning')
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/verify_email/<token>')
def verify_email(token):
    try:
        email = serializer.loads(token, salt='email-confirm-salt', max_age=3600)
        student = Student.query.filter_by(email=email).first_or_404()
        student.is_verified = True
        db.session.commit()
        flash('Your account has been verified. You can now log in.', 'success')
        return redirect(url_for('login'))
    except:
        flash('The verification link is invalid or has expired.', 'danger')
        return redirect(url_for('signup'))

@app.route('/student_portal')
@login_required
def student_portal():
    return render_template('student_portal.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome'))

# Helper Functions
def send_verification_email(email, token):
    msg = Message('Verify your Email', sender='noreply@demo.com', recipients=[email])
    link = url_for('verify_email', token=token, _external=True)
    msg.body = f'Please click the following link to verify your account: {link}'
    mail.send(msg)

# Run the app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

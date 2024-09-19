# prompt: "Write a Python script that sends an email using Gmail's SMTP server. The script should use the smtplib library to connect securely using TLS on port 587. The email should include both subject and body text, formatted using the email.mime module. It should also handle any potential errors during the connection, authentication, or email-sending process. Ensure to explain how to set up an app-specif

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
  """
  Sends an email using Gmail's SMTP server.

  Args:
    sender_email: The sender's email address.
    sender_password: The sender's email password.
    receiver_email: The recipient's email address.
    subject: The email subject.
    body: The email body text.
  """
  try:
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the sender's account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the connection
    server.quit()

    print("Email sent successfully!")

  except Exception as e:
    print(f"Error sending email: {e}")

# Example usage
sender_email = "ijlalkhanzada@gmail.com"
sender_password = "eqet jvrc kljz xwjs"
receiver_email = "ijlalkhanzada1989@gmail.com"
subject = "Test Email"
body = """
    Dear [Recipient's Name],

    I hope this email finds you well. As a professional specializing in Autonomous AI Agent Development, I would like to express my interest in exploring opportunities for collaboration.

    My expertise lies in designing and implementing autonomous AI agents that operate across various domains, from decision-making systems to machine learning-driven environments. With a strong background in AI, I am confident that we can create impactful solutions tailored to emerging needs in the field.

    I would appreciate the opportunity to discuss potential projects where we can combine our expertise to drive innovation forward. Please feel free to reach out at your convenience to schedule a discussion.

    Thank you for your time, and I look forward to hearing from you.

    Best regards,
    [Your Name]
    Autonomous AI Agent Developer
    """

send_email(sender_email, sender_password, receiver_email, subject, body)


# Setting up an app-specific password:

# 1. Go to your Google Account security settings.
# 2. Under "Signing in to Google", find the "App passwords" section.
# 3. Select "Select app" and choose "Mail".
# 4. Choose "Select device" and select your device.
# 5. Click "Generate".
# 6.  You'll be given a 16-character app password. Use this password in the script instead of your regular email password.

import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_email_content(profession, recipient_name):
    """ 
    پروفیشن کے حساب سے ای میل کا مواد تیار کریں۔
    """
    if profession == 'Doctor':
        subject = "Collaboration in Healthcare AI Solutions"
        body = f"""
        Dear Dr. {recipient_name},

        I hope this message finds you well. As an expert in healthcare solutions, I would like to explore AI applications in your field.

        Let's discuss how we can work together on healthcare innovations powered by AI.

        Best regards,
        Alice Johnson
        AI Solutions Developer
        """
    elif profession == 'Engineer':
        subject = "Engineering AI Collaboration Opportunity"
        body = f"""
        Dear Engr. {recipient_name},

        I hope you are doing well. I would like to collaborate on AI-driven engineering projects that could enhance industrial automation.

        Please feel free to reach out to discuss further.

        Best regards,
        Alice Johnson
        Autonomous AI Agent Developer
        """
    elif profession == 'Teacher':
        subject = "AI Solutions for Education"
        body = f"""
        Dear {recipient_name},

        As a professional in education, we would like to explore AI solutions to enhance learning experiences for students.

        Let’s connect and discuss how AI can be integrated into education.

        Best regards,
        Alice Johnson
        AI Developer for Education
        """
    else:
        subject = "Collaboration Opportunity"
        body = f"""
        Dear {recipient_name},

        I would love to discuss collaboration opportunities in the field of AI. Please reach out at your earliest convenience.

        Best regards,
        Alice Johnson
        AI Expert
        """
    
    return subject, body

def send_email(sender_email, password, recipient_email, recipient_name, subject, body):
    """
    ای میل بھیجنے کا فنکشن
    """
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print(f"Email sent successfully to {recipient_name} ({recipient_email})")
    except Exception as e:
        print(f"Error sending to {recipient_email}: {e}")
    finally:
        server.quit()

def send_bulk_emails(sender_email, password, excel_file_path):
    """
    ایکسل فائل پڑھ کر سب کو ای میل بھیجنے کا فنکشن
    """
    df = pd.read_excel(excel_file_path)

    for index, row in df.iterrows():
        recipient_email = row['Email']
        recipient_name = row['Name']
        profession = row['Profession']
        
        subject, body = get_email_content(profession, recipient_name)
        send_email(sender_email, password, recipient_email, recipient_name, subject, body)

# مثال کے طور پر استعمال کریں
if __name__ == "__main__":
    sender_email = "ijlalkhanzada@gmail.com"
    password = "eqet jvrc kljz xwjs"
    excel_file_path = "recipients.xlsx"  # ایکسل فائل کا راستہ
    
    send_bulk_emails(sender_email, password, excel_file_path)
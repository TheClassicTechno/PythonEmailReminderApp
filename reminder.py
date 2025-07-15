import smtplib
import schedule
import time
from email.message import EmailMessage


EMAIL_ADDRESS = 'juliah6169@gmail.com'        
EMAIL_PASSWORD = 'BLANK'        

TO_EMAIL = 'juliah6169@gmail.com'           
SUBJECT = 'Reminder: Meeting at 10 AM'
BODY = 'Hi! Just a quick reminder: meeting is at 10 AM!'


def send_reminder():
    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg.set_content(BODY)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(" Reminder sent successfully")
    except Exception as e:
        print(f" Failed to send email: {e}")


schedule.every().day.at("22:26").do(send_reminder)

print("Email scheduler started")

while True:
    schedule.run_pending()
    time.sleep(60)

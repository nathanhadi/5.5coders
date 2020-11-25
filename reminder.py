import smtplib, ssl
from email.mime.text import MIMEText
from datetime import date
import backend

user = "testing1"

def send_reminder(sender_email, receiver_email, message):
    """
    Sends a user an email with the specified message.

    @param receiver_email: Email to send to.
    """
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = "ilovecoding2020!"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email successfully sent.")

def main():
    sender_email = "cs465.5.5coders@gmail.com"
    receiver_email = "testingcs465@gmail.com"
    
    today = date.today()
    readings = backend.get_readings(user)

    message = "Hi " + user + ", These are your current goals and readings:\n\n"

    for i in readings:
        message += "         - Title: " + i['Title'] + " | Number of pages: " + i['Reading']['Pages'] + " Number of chapters: " + i['Reading']['Chapters'] + " | Goal Name: " + i['Goal']['Name'] + " by " + i['Goal']['Date'] + "\n"

    msg = MIMEText(message)
    msg['Subject'] = 'Reading Reminder ' + today.strftime("%m/%d/%Y")
    msg['From'] = sender_email
    msg['To'] = receiver_email

    send_reminder(sender_email, receiver_email, msg)

if __name__ == "__main__":
    main()
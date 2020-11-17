import smtplib, ssl
from email.mime.text import MIMEText


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

    msg = MIMEText('MESSAGE')
    msg['Subject'] = 'Test mail'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    send_reminder(sender_email, receiver_email, msg)

if __name__ == "__main__":
    main()
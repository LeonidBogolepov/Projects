import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


if __name__ == "__main__":
    EmailSendTo = input("Enter address to send email: ")
    print(EmailSendTo)
    EmailCome  = input("Enter address from email will be recived: ")
    print(EmailCome)
    Password = input("Enter password: ")
    print(Password)
    Title = input("Enter title: ")
    print(Title)
    Body = input("Enter body: ")
    print(Body)
    strgap =input("Enter the gap: ")
    gap=int(strgap)
    print(gap)
    MIME = MIMEMultipart()
    MIME['From'] = EmailCome
    MIME['To'] = EmailSendTo
    MIME['Date'] = formatdate(localtime=True)
    MIME['Subject'] = Title
    while True:
        try:
            server_ssl = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
            server_ssl.ehlo()
            server_ssl.login(EmailCome, Password)
            server_ssl.sendmail(MIME['From'], MIME['To'], MIME.as_string())
            server_ssl.close()
            print('email was sented')
        except Exception:
            print("message sending in progress")
        time.sleep(gap)


import smtplib

SENDER_EMAIL = "fenixfirea380@gmail.com"
PASSWORD = "windranger"
SMTP_ADDRESS = "smtp.gmail.com"


class MailSender:
    """class to send emails"""
    def __init__(self):
        self.email = SENDER_EMAIL
        self.password = PASSWORD
        self.smtp = SMTP_ADDRESS

    def send_mail(self, to_address, message):
        """sends email to the given email address"""
        with smtplib.SMTP(self.smtp) as connection:
            connection.starttls()
            connection.login(user=self.email,
                             password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=to_address,
                                msg=message.encode('utf-8'))
            print("mail sent successfully")

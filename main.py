from scraper import Scraper
from mailsender import MailSender


scraper = Scraper()
mail_sender = MailSender()

# AT WHAT PRICE YOU WANT THAT THING 
MY_PRICE = 25000

price, title = scraper.get_price()
print(price)
print(title)

# IF THE ORIGINAL PRICE IS LESS THAN THE PRICE YOU"VE MENTIONED AN EMAIL IS SENT TO YOU
if price <= MY_PRICE:
    message = f"Subject: Low Price Alert\n\nThe price of {title} is now only ₹{price}\n\nclick the link below to buy\n\n{scraper.url}"
    receiver_email = "aditya.chache@gmail.com"
    mail_sender.send_mail(to_address=receiver_email,
                          message=message)





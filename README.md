# Amazon-price-tracker

## Sends you an Email alert whenever the price of any item you've mentioned drops below a certain price.

![image](https://user-images.githubusercontent.com/84438200/153756116-d167c378-3d6b-4cde-ac5d-31c8f8229004.png)


To use this you need to mention the link of the url of the thing you want, the price you want to buy it, your email and password to send email alerts


1.  In `main.py` you can set the price
![image](https://user-images.githubusercontent.com/84438200/153756202-2c0a3c53-f065-42a1-9e2e-14c5e2c551fb.png)


2. In `scraper.py` you need to paste the url of the product
![image](https://user-images.githubusercontent.com/84438200/153756242-9f2cbfb1-226d-4731-b7c4-31f44dda3154.png)


3. In `mainsender.py` make the following changes
![image](https://user-images.githubusercontent.com/84438200/153756301-4e5531af-23ff-46ac-9a97-134ce7afebf4.png)


**After making these changes run the `main.py` file**


**if you're getting errors then there maybe 2 possible reasons**

1. there maybe some errors while sending mails (2 fac authentication should be off, lower security apps should be granted permissions, etc in order for emails to work)

2. If Amazon have changed their website structure then the `scraper.py` script won't work. In that case we'll need to make changes in our code.

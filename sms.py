import os
import getpass
# lib for sending emails with smtp
import smtplib, ssl
from email.message import EmailMessage
import imghdr
# lib for sending sms with twilio API
# from twilio.rest import Client
# lib for whatsapp bot with web flow control
from selenium import webdriver
from time import sleep



# Twilio section
# # sending sms with API twilio
# account_sid = os.environ["sid"]
# auth_token = os.environ["tok"]
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#                             messaging_service_sid='MG0c8f77db540fe880110b5a458ec2ba30', 
#                             to='+447500512084',
#                             body= 'hi this is sms demo from waky waky ?? if you get it please text me back on facebook.'      
#                           )
# print(message.sid)
# print('Massage has been sent!')
 
 # sending email with attach jpag
# subject = str(input('input your title: '))
# body = str(input('Input your massage: '))
 
# port = 465 #SSL Connection
# smtp_server = "smtp.gmail.com"
# sender_email = "bugdev91@gmail.com"
# receiver_email = "leonvita91@gmail.com"
# password = 'hmgegfcuwlqefjsp'

# msg = EmailMessage()
# msg['Subject'] = subject
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg.set_content(body)

# # attach & declear the img data
# with open('pic.jpg','rb') as f:
#     file_read = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name
#     print(file_type)

# msg.add_attachment(
#     file_read, maintype='image',subtype=file_type, filename = file_name
# )
# # secure the connection
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port , context=context) as server:
#     # login and sending
#     server.login(sender_email, password)
#     server.send_message(msg)



# Dic informations 
# CHROME_PROFILE_PATH = "user-data-dir=Users/akjasim/Library/Application Support/Google/Chrome/Wtsp"

user = getpass.getuser()
sys = {
    'windows' : f"user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default",
    'mac'   : f"user-data-dir=Users/{user}/Library/Application Support/BraveSoftware/Brave-Browser/wts",
    'linux'     : f"user-data-dir=/home/{user}/.config/google-chrome/default"
}

print(sys['windows'])
print(sys['mac'])
print(sys['linux'])


driver_path = "/opt/homebrew/bin/chromedriver"
brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_experimental_option('detach', True)
option.add_argument(sys['mac'])
driver = webdriver.Chrome(executable_path=driver_path, options=option)
# Create new Instance of Chrome
driver.get("https://web.whatsapp.com")
sleep(10)


driver.close()
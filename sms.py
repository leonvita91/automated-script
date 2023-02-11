import os
from twilio.rest import Client


# Twilio section
# sending sms with API twilio
account_sid = os.environ["sid"] # sid
auth_token = os.environ["tok"] # API Token
client = Client(account_sid, auth_token)
message = client.messages.create(
                            messaging_service_sid='MG0c8f77db540fe880110b5a458ec2ba30', 
                            to='+447500512084',
                            body= 'Here comes the demo massage from Tw to anynumber.'      
                          )
print(message.sid)
print('Massage has been sent!')
 
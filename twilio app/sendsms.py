from twilio.rest import Client
from Credentials import Account_sid, auth_token, my_cell, my_twilio
client = Client(Account_sid, auth_token)
my_msg = ''.join(['Hello!\n' for i in range(15)])
message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
print(message)

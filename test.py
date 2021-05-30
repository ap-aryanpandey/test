import os
from twilio.rest import Client

def comm():
    account_sid = 'AC62d7373283aef2f0b49837d2e0680ee1'
    auth_token = '2ca2bbc9aa841f91ca4b6b5e9118c9d9'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                            from_='whatsapp:+14155238886',
                            body='Hello, there!',
                            to='whatsapp:+918853056579'
                        )

    print(message.sid)

call =comm()
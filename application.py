import json
import requests
import os
from twilio.rest import Client


def send_message():
    api_url = 'https://api.quotable.io/random'
    quote = ''
    response = requests.get(api_url)
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    print('account_sid', account_sid)
    print('auth_token', auth_token)
    client = Client(account_sid, auth_token)
    from_phone = os.environ['FROM_PHONE']
    to_phone = os.environ['TO_PHONE']
    print('from_phone', from_phone)
    print('to_phone', to_phone)


    if response.status_code == 200:
        contents = json.loads(response.content.decode('utf-8'))
        quote = contents['content']
        author = contents['author']
        body = '"' + quote + '" - ' + author
        message = client.messages.create(
            body=body,
            from_=from_phone,
            to=to_phone
        )
        print('success', message.sid)

send_message()
import requests
import time
import os
from dotenv import load_dotenv 
from twilio.rest import Client


def get_status(user_id):
    load_dotenv()
    token = os.getenv('token_vk')
    params = {
        'user_ids' : user_id,
        'access_token' : token,
        'v':5.103,
        'fields':'online',
    }
    url = 'https://api.vk.com/method/users.get'
    status = requests.post(url=url, params=params)
    return status.json()['response'][0]['online']



def sms_sender(sms_text):
    load_dotenv()
    account_sid = os.getenv('sid_twilio')
    auth_token = os.getenv('token_twilio')
    NUMBER_FROM = os.getenv('NUMBER_FROM')
    NUMBER_TO = os.getenv('NUMBER_TO')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body=sms_text,
                              from_=NUMBER_FROM,
                              to=NUMBER_TO
                          )
    return message.sid  # Верните sid отправленного сообщения из Twilio 642 153 


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
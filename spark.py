import json

import requests

from settings import CONFIG

'''
Get the Spark URL from settings file
'''


def spark_url():
    return CONFIG["SPARK_URL"]


'''
Get Spark Message based on ID
Return either the message text or 'none' if message was not directed to the Spark Bot
'''


def get_message(message_id, bearer=CONFIG['BEARER'], bot=CONFIG['BOT_ID']):
    apiHeader = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + bearer
    }

    resp = requests.get(spark_url() + '/v1/messages/' + message_id, headers=apiHeader)
    data = resp.json()
    for person in data['mentionedPeople']:
        if person == bot:
            return data['text']
    return ''


'''
Send a message to a Spark room from the Bot
Return True if the message is sent successfully
'''


def send_message(message, room_id=CONFIG['ROOM_ID'], bearer=CONFIG['BEARER']):
    apiHeader = {
        'Authorization': 'Bearer ' + bearer,
        "Content-Type": "application/json"
    }

    newMessage = json.dumps({
        'roomId': room_id,
        'text': message

    })

    resp = requests.post(spark_url() + '/v1/messages/', headers=apiHeader, data=newMessage)
    return resp.status_code

import datetime
import logging

import requests

import spark
from botTriggers import BOT_DICTIONARY

'''
Main Bot Logic
Reads and responds to messages addressed to the Bot in the spark room
'''


def spark_bot(msg_id):
    logging.basicConfig(filename='spark_bot_logs.log', level=logging.DEBUG)
    logging.debug(time_stamp() + ' New Web Hook Request, message ID: ' + str(msg_id))

    #   Bot Dictionary defines phrases that will trigger different actions and responses for the bot
    # If no valid trigger phrase is sent, use the default action and response
    response = BOT_DICTIONARY['defaults']['response']
    action = BOT_DICTIONARY['defaults']['action']

    try:

        #   Look up message in spark
        message = spark.get_message(msg_id)
        if message == '':
            logging.warning(time_stamp() + ' Failed to retrieve messafe from spark, message ID: ' + msg_id)

        # Check bot dictionary for a matching trigger phrase
        for key in BOT_DICTIONARY['triggers']:
            for trigger in key['trigger']:
                if trigger in message.lower():
                    action = key['action']
                    response = key['response']

        # Act and respond based on trigger phrases
        if action == 'add vlan':

            spark.send_message(response)

            '''
                Add prime logic here
                Example:
                vlanId = screenScraper.get_vlan(message)
                response = primeInfrastructure.create_config_vlan_model(vlanId)
                state = spark.send_message(response)
            
            '''

        elif action == 'add ap':
            spark.send_message(response)

            '''
                Add Prime logic here
            '''

        else:
            spark.send_message(response)

    except requests.exceptions.RequestException as e:
        logging.warning(time_stamp() + ' ' + str(e))


def time_stamp():
    return datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")

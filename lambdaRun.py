from bot import spark_bot as run_bot

'''
Web Hook activated spark bot
Run this module for for AWS Lambda implementation
'''
def lambda_handler(event, context):
    msgId = event['data']['id']
    run_bot(msgId)

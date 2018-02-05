from flask import Flask, request

from bot import spark_bot as run_bot

app = Flask(__name__)

'''
Web Hook activated spark bot
Run this module for traditional implementation using Flask
'''


@app.route('/Spark-WH', methods=['POST'])
def spark_bot():
    data = request.json
    msgId = data['data']['id']

    run_bot(msgId)

    return ('', 200)


@app.route('/todo/api/v1.0/test', methods=['GET'])
def get_tasks():
    return "Hello World"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

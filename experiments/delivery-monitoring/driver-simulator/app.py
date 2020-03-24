import json
import pika
import time
import _thread

from flask import Flask
from flask import jsonify

app = Flask(__name__)

def __connection_rabiitmq():
    credentials = pika.PlainCredentials(username='admin', password='admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    return connection

def __load_drivers():
    with open('drivers.json') as file:
        return json.load(file)

def __simulator(name, id):
    filename = 'destination/' + str(id) + '.txt'
    with open(filename) as file:
        lines = file.readlines()

        connection = __connection_rabiitmq()
        channel = connection.channel()
        channel.queue_declare(queue='driver_location')

        for line in lines:
            time.sleep(2)
            print(line)
            channel.basic_publish(exchange='', routing_key='driver_location', body=line.strip())

        connection.close()

def __callback(_channel, method, properties, body):
    print(body.decode())
    _thread.start_new_thread(__simulator, ('simulation', body.decode()))

def __consuming():
    connection = __connection_rabiitmq()
    channel = connection.channel()
    channel.queue_declare(queue='simulation')
    channel.basic_consume('simulation', __callback, auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    __consuming()
    app.run()

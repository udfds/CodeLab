import pika
import time
from random import randrange

credentials = pika.PlainCredentials(username='admin', password='admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(_channel, method, properties, body):
    print(" [x] Received %r" % body)

    # Remove 'auto_ack' from 'basic_consume' to enable manual ack
    # time.sleep(randrange(0, 5))
    # print(" [x] Done")
    # _channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume('hello', callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
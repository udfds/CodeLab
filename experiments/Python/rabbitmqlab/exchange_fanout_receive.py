import pika
import time

# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

# Exchanges
# Type fanout: All queues receive the message
# Type direct: The routing key define the queue
# Type topic: The queues is defined by the expression of routing key
# Type header: The queue is defined by the header of message
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

def callback(_channel, method, properties, body):
    print('Message received:', body)
    
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()


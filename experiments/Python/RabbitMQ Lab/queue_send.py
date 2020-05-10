import pika
import sys

# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

# Declare a queue with messages durable
channel.queue_declare(queue='task_queue', durable=True)

# Get the message from terminal or use the 'Hello World!'
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Make the message persistent
message_properties = pika.BasicProperties(delivery_mode=2,)
channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=message_properties)

print('Sent: ', message)
connection.close()
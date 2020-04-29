import pika
import sys

# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Get the message from terminal or use the 'Exchange message!'
message = ' '.join(sys.argv[1:]) or "Exchange message!"

channel.basic_publish(exchange='logs', routing_key='', body=message)

print("Sent: ", message)
connection.close()
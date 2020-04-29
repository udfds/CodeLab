import pika
import sys

# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Exchange direct!'

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)

print('Sent:', message)
connection.close()

# Execution
# python exchange_direct_send.py [type of message] "Message N"
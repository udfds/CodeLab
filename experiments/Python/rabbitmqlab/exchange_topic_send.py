import pika
import sys

# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Exchange topic!'

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

print('Sent:', message)
connection.close()

# Execution
# python exchange_topic_send.py "kern.critical" "Message critial"
# python exchange_topic_send.py "kern.warnning" "Message warnning"
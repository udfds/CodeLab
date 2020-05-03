import pika
import sys

# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write('Error:', sys.argv[0])
    sys.exit(1)

# Create a queue for each keys(routing_key) received by the arguments
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

def callback(_channel, method, properties, body):
    print('Message received:', body)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()

# Execution
# python exchange_topic_receive.py "#" 
# python exchange_topic_receive.py "kern.*"  
# python exchange_topic_receive.py "*.critical"  
# python exchange_topic_receive.py "kern.*" "*.critical"  
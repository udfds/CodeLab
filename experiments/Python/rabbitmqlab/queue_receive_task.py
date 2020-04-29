import pika
import time

# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

# Declare a queue with messages durable
channel.queue_declare(queue='task_queue', durable=True)

def callback(_channel, method, properties, body):
    print('Message received:', body)
    time.sleep(body.count(b'.'))
    print('Done..')
    # Send the ACK to RabbitMQ delete the message
    _channel.basic_ack(delivery_tag=method.delivery_tag)
    
# Configure worker to not receive new message until finish the current
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print("Waiting for messages...")
channel.start_consuming()



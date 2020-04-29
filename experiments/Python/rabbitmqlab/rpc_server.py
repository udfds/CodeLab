import pika 


# Define the credentials of RabbitMQ
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fibonacci(number):
    if number == 0:
        return 0
    elif number ==1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def callback(_channel, method, properties, body):
    number = int(body)
    print('Value received:', number)

    message_properties = pika.BasicProperties(correlation_id = properties.correlation_id)
    response = fibonacci(number)
    channel.basic_publish(exchange='', routing_key=properties.reply_to, properties=message_properties, body=str(number))
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=callback)

print('Waiting for messages...')
channel.start_consuming()

# Execution
# python exchange_direct_receive.py error warning info > messages_from_rabbitmq.log
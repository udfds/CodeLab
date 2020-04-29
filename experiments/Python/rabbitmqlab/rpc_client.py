import pika
import uuid

class RPC_Client(object):

    def __init__(self):
        # Define the credentials of RabbitMQ
        self.credentials = pika.PlainCredentials(username='guest', password='guest')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673, credentials=self.credentials))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(queue=self.callback_queue, on_message_callback=self.callback, auto_ack=True)
    
    def callback(self, _channel, method, properties, body):
        if self.correlation_id == properties.correlation_id:
            self.response = body
    
    def call(self, number):
        self.response = None
        self.correlation_id = str(uuid.uuid4())

        message_properties = pika.BasicProperties(reply_to=self.callback_queue, correlation_id=self.correlation_id,)
        self.channel.basic_publish(exchange='', routing_key='rpc_queue', properties=message_properties, body=str(number))

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)

client = RPC_Client()

print('Sent:', 0)
response = client.call(0)
print('Received:', response)



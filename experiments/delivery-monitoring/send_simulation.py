import pika

credentials = pika.PlainCredentials(username='admin', password='admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='simulation')

channel.basic_publish(exchange='',
                      routing_key='simulation',
                      body='1')

print(" [x] Sent 'Hello World!'")
connection.close()




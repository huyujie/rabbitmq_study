# -*-coding:utf-8-*-

import pika

# build a connection to rabbitmq server
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     host='127.0.0.1'))
channel = connection.channel()

# build a queue
channel.queue_declare(queue='hello')

# exchange is default, routing_key must equal to queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()


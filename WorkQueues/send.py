# -*-coding:utf-8-*-

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     host='localhost'))
channel = connection.channel()

# declare queue is durable
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      # make message persistent
                      properties=pika.BasicProperties(delivery_mode = 2,)
                     )
print " [x] Sent %r" % (message,)
connection.close()
